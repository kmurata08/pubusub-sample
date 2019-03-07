from google.cloud import pubsub_v1
from dotenv import load_dotenv
import os


def loadenv():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    
def get_project_id():
    loadenv()
    return os.environ.get('PROJECT_ID')


def get_topic_name():
    loadenv()
    return os.environ.get('TOPIC_NAME')


def main():
    project_id = get_project_id()
    topic_name = get_topic_name()

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    for n in range(1, 10):
        data = u'Message number {}'.format(n)
        data = data.encode('utf-8')
        publisher.publish(topic_path, data=data)

    print('Published messages.')


if __name__ == '__main__':
    main()
