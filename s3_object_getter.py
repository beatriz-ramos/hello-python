import boto3

# Let's use Amazon S3
# pip3 install boto3
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
