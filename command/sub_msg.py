from google.cloud import pubsub_v1
from dotenv import load_dotenv
import os, time


def loadenv():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)


def get_project_id():
    loadenv()
    return os.environ.get('PROJECT_ID')


def get_subscription_name():
    loadenv()
    return os.environ.get('SUBSCRIPTION_NAME')


def callback(message):
    print('Received message: {}'.format(message))
    message.ack()

    
def main():
    project_id = get_project_id()
    subscription_name = get_subscription_name()

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(
        project_id, subscription_name)

    subscriber.subscribe(subscription_path, callback=callback)

    print('Listening for messages on {}'.format(subscription_path))
    while True:
        time.sleep(10)
    

if __name__ == '__main__':
    main()
