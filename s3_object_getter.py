import boto3
from datetime import datetime as datetime
from datetime import timedelta as timedelta
from datetime import timezone as timezone

# Let's use Amazon S3
# pip3 install boto3
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
s3 = boto3.resource('s3')
bucket_name = 'uux-itaas-packager-catalog-data'
prefix = 'archive/dev'
expire_date = datetime.now(timezone.utc) - timedelta(days=365)

bucket = s3.Bucket(bucket_name)

# Print out bucket objects
for bucket_object in bucket.objects.all():
    if bucket_object.key.startswith(prefix) and bucket_object.last_modified <= expire_date:
        print(bucket_object)
