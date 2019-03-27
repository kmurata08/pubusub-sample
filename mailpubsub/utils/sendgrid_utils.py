import sendgrid
from sendgrid.helpers.mail import Email, Content, Mail
from dotenv import load_dotenv
import os
import textwrap


def loadenv():
    dotenv_path = os.path.join(os.path.dirname(
        os.path.dirname(__file__)), '.env')
    load_dotenv(dotenv_path)


def get_api_key():
    loadenv()
    return os.environ.get('SENDGRID_API_KEY')


def send_mail(to_email, subject, message):
    sg = sendgrid.SendGridAPIClient(apikey=get_api_key())

    content_message = get_content_message(to_email, message)

    mail = Mail(
        Email('pubsubtest@test.com'),
        subject,
        Email(to_email),
        Content('text/plain', content_message))

    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    if response.status_code >= 400:
        return False

    return True


def get_content_message(to_email, message):
    content = textwrap.dedent('''
    {email}様

    フォームに入力いただきありがとうございます。

    {email}様の一言は、{message}です。
    ''').format(email=to_email, message=message).strip()

    return content
