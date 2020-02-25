
import base64

def wallme(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

