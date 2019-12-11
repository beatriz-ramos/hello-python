import boto3
s3 = boto3.client('s3')


def list_expired_objects(bucket_name, prefix, expire_date):
    print(f'Listing files from bucket {bucket_name} with date older than {expire_date}')
    for bucket_object in get_objects(bucket_name, prefix):
        object_key = bucket_object['Key']

        if object_key.startswith(prefix) and bucket_object['LastModified'] <= expire_date:
            print(object_key)


def get_objects(bucket_name, prefix):
    return s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)['Contents']