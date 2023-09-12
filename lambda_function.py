import os
from download import download_file
from util import get_and_check_bookmark,upload_bookmark_file
from upload import upload_file

def lambda_handler(event, context):
    # check the environment
    environ=os.environ.get('ENVIRON')
    
    #check if the profile is 'DEV'
    if environ == 'DEV':
        print(f'Running using {environ} environment')

    # os.environ.setdefault('AWS_PROFILE','zy-udemy-admin')
    # os.environ.setdefault('AWS_DEFAULT_REGION','ap-southeast-1')

    # get the file store in environment
    bucket_name=os.environ.get('BUCKET_NAME')
    bookmark_file = os.environ.get('BOOKMARK_FILE')
    bookmark_name = os.environ.get('BOOKMARK_NAME')
    token = os.environ.get('token')

    # check the latest bookmark

    checking_result = get_and_check_bookmark(bucket_name,bookmark_file,bookmark_name)
    if checking_result == 'Latest':
        print('-----------We got the latest data for the today----------')
        return print('Data is the latest, no updated needed')
    else:
        print('-----------Download the latest data-----------')
        # download the file 
        repos_organization = download_file(token=token)
        
        print('-----------Upload the latest data to s3-----------')
        # upload to s3
        upload_file(repos_organization=repos_organization,bucket_name=bucket_name)

        print('-----------Updating bookmark----------')
        upload_bookmark_file(bucket_name,bookmark_file,bookmark_name)
        return print('Data updated')
        