import boto3
import json
from datetime import datetime
from botocore.errorfactory import ClientError

def get_client():
    return boto3.client('s3')

def upload_bookmark_file(bucket_name,bookmark_file,bookmark_name):

    s3_client = get_client()
    
    # Get the current date and time
    current_datetime = datetime.now()
    
    # Get the date portion only
    current_date = current_datetime.date()
    
    # Convert the date to a string with a custom format
    date_string = current_date.strftime('%Y-%m-%d')

    # have the details of the latest data
    bookmark_details = {
        'Date_of_access':f'{date_string}',
        'Owner':'Zhi Yong',
        'Company included':['microsoft','Google','facebook','Apple', 'Netflix']
    }

    json_data = json.dumps(bookmark_details)

    # put the object to s3
    s3_client.put_object(
        Bucket=bucket_name,
        Key=f'{bookmark_file}/{bookmark_name}',
        Body=json_data,
        ContentType='application/json'
    )
    print('Putting lastest bookmark done')

def get_and_check_bookmark(bucket_name,bookmark_file,bookmark_name):

    s3_client = get_client()
    
     # Get the current date and time
    current_datetime = datetime.now()
    
    # Get the date portion only
    current_date = current_datetime.date()
    
    # Convert the date to a string with a custom format
    date_string = current_date.strftime('%Y-%m-%d')
    
    try:
        response = s3_client.get_object(
            Bucket=bucket_name,
            Key=f'{bookmark_file}/{bookmark_name}'
        )

        if json.loads(response['Body'].read().decode('utf-8'))['Date_of_access'] == date_string:
            print('-----------The data is up-to-date-----------')

            Checking_result = 'Latest'
            
            return Checking_result
            
        else:
            # upload_bookmark_file(bucket_name,bookmark_file,bookmark_name)
            print('------------The latest data is not updated, kindly download the latest data----------')

            Checking_result ='New data needed'
            return Checking_result
            
    except ClientError as e:
        if e.response['Error']['Code']== 'NoSuchKey':
            # upload_bookmark_file(bucket_name,bookmark_file,bookmark_name)
            print('----------No bookmark file available, kindly download the data through Github Api----------')
            Checking_result ='New data needed'
            return Checking_result
            
            