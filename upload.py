from util import get_client
import json


def upload_file(repos_organization,bucket_name):

    s3_client = get_client()
    
    for i in range (len(repos_organization)):

        organization_name = repos_organization[i][0]['owner.login']
        s3_object_key = f'latest-100-repo/{organization_name}.json'
        
        json_data = '\n'.join(json.dumps(record) for record in repos_organization[i])

        response = s3_client.put_object(
            Bucket=bucket_name,
            Key=s3_object_key,
            Body=json_data
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(f'Upload for {organization_name} completed!')
        else:
            print(f'Upload for {organization_name} failed!')
        