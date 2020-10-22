import boto3
import json
from fake_web_events import Simulation


client = boto3.client('kinesis')


def put_record(event):
    data = (json.dumps(event) + '\n').encode('utf-8')
    response = client.put_record(
        StreamName='kinesis-stream',
        Data=data,
        PartitionKey='test'
    )
    return response


simulation = Simulation(user_pool_size=200, sessions_per_day=15000
events = simulation.run(duration_seconds=600)

for event in events:
    put_record(event)
