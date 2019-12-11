import boto3
from s3_object_lister import get_objects
s3 = boto3.client('s3')


def clean_expired_objects(bucket_name, prefix, expire_date):
    print(f'Deleting files from bucket {bucket_name}')
    print()
    for bucket_object in get_objects(bucket_name, prefix):
        obj_key = bucket_object['Key']

        if obj_key.startswith(prefix) and bucket_object['LastModified'] <= expire_date:
            s3.delete_object(Bucket=bucket_name,Key=obj_key)
            print(f'Deleted object {obj_key}')