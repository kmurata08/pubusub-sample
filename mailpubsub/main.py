from flask import Flask, render_template, request, redirect, url_for
from utils import push_to_topic, pull_from_subscriber

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mail/push', methods=['POST'])
def mail_push():
    email = request.form['email']
    message = request.form['message']

    push_msg = 'Email: %s, Message: %s' % (email, message)
    push_to_topic(push_msg)

    return redirect(url_for('index'))


@app.route('/mail/pull')
def mail_pull():
    pull_from_subscriber()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
