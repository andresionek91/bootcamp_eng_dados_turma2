from aws_cdk import core
from aws_cdk import (
    aws_s3 as s3
)

class S3Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        encryption = s3.BucketEncryption(s3.BucketEncryption.S3_MANAGED)
        s3.Bucket(self, 'meu-bucket-belisco-cdk', bucket_name='meu-bucket-belisco-cdk', encryption=encryption)
