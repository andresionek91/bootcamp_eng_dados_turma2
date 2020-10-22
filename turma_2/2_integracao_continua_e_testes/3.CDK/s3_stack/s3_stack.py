from aws_cdk import core
from aws_cdk import (
    aws_s3 as s3
)
import enum


class Encryption(enum.Enum):
    S3_MANAGED = 1


class S3Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        encryption = s3.BucketEncryption(Encryption.S3_MANAGED)
        s3.Bucket(self, 'meu-bucket-belisco-cdk', bucket_name='meu-bucket-belisco-cdk', encryption=encryption)
