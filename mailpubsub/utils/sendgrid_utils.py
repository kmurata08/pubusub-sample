import sendgrid
from sendgrid.helpers.mail import Email, Content, Mail
from dotenv import load_dotenv
import os


def loadenv():
    dotenv_path = os.path.join(os.path.dirname(
        os.path.dirname(__file__)), '.env')
    load_dotenv(dotenv_path)


def get_api_key():
    loadenv()
    return os.environ.get('SENDGRID_API_KEY')


def send_mail(to_email, message):
    sg = sendgrid.SendGridAPIClient(apikey=get_api_key())
    from_email = Email('mrt014kzm@gmail.com')
    subject = 'Test Email'
    content = Content('text/plain', message)
    mail = Mail(from_email, subject, Email(to_email), content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
