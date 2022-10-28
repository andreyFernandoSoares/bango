import boto3
import json

sqs_client = boto3.client("sqs", region_name="us-east-1")

queue_name = 'movie'

def get_queue():
    queue = sqs_client.get_queue_url(QueueName=queue_name)
    return queue["QueueUrl"]

def lambda_handler(event, context):
    queue = get_queue()

    message = {"1": "Alto filmao hoje"}

    response = sqs_client.send_message(
        QueueUrl=queue,
        MessageBody=json.dumps(message)
    )

    print(response)