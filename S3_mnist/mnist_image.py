import boto3
s3_client = boto3.client('s3')
s3_client.upload_file('jib-mnist:0.0.${BUILD_NUMBER}', 'jibigbucket', 'jib-mnist:0.0.${BUILD_NUMBER}')