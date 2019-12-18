import sys
from datetime import datetime as datetime
from datetime import timedelta
from datetime import timezone
from s3_object_cleaner import clean_expired_objects
from s3_object_lister import list_expired_objects


# Let's use Amazon S3
# pip3 install boto3
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html


def get_arg(index, default_value=''):
    if len(sys.argv) <= index:
        return default_value
    return sys.argv[index]


mode = get_arg(1)
prefix = get_arg(2, 'archive/dev')
max_days = get_arg(3, 365)

bucket_name = 'uux-itaas-packager-catalog-data'
expire_date = datetime.now(timezone.utc) - timedelta(days=int(max_days))

if mode.lower() == 'clean':
    clean_expired_objects(bucket_name, prefix, expire_date)
if mode.lower() == 'list':
    list_expired_objects(bucket_name, prefix, expire_date)

print()
print('Done!')