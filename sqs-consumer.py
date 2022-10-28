import boto3

sqs = boto3.resource('sqs')

queue_name = 'movie'

def get_queue():
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    return queue

def lambda_handler(event, context):
    queue = get_queue()

    messages = queue.receive_messages(
        MessageAttributeNames=['All'],
        MaxNumberOfMessages=10,
        WaitTimeSeconds=2
    )

    for msg in messages:
        print(msg.body)