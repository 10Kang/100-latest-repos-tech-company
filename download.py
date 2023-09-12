import requests 
import json

def get_repos_retails(repos):
    
    repos_details = []

    # loop to each repo of the organization 
    for i in range (len(repos)):
        repo_details = {'id':repos[i]['id'],
                            'node_id':repos[i]['node_id'],
                            'name':repos[i]['name'],
                            'full_name':repos[i]['full_name'],
                            'owner.login': repos[i]['owner']['login'],
                            'owner.node_id':repos[i]['owner']['node_id'],
                            'owner.type':repos[i]['owner']['type'],
                            'owner.site_admin':repos[i]['owner']['site_admin'],
                            'html_url':repos[i]['html_url'],
                            'description':repos[i]['description'],
                            'fork':repos[i]['fork'],
                            'created_at':repos[i]['created_at'],
                            'watchers_count': repos[i]['watchers_count'],
                            'forks_count':repos[i]['forks_count'],
                            'language':repos[i]['language'],
                            'stargazers_count':repos[i]['stargazers_count']}
        
        repos_details.append(repo_details)

    return repos_details


def download_file(token):
    '''
    organization = list of organization to access their data in github

    token = Github Token 

    '''
    organization=['microsoft','Google','facebook','Apple', 'Netflix']
    
    repos_organization = []
    
    for i in range (len(organization)):
        
        api_url = f"https://api.github.com/orgs/{organization[i]}/repos"
        headers = {'Authorization': f'token {token}'}
        params = {
            "page": 1,
            "per_page": 100,
            "sort": "created",
            "direction": "desc"}

        # get the responses of listing the repo of certain organizations
        response = requests.get(api_url, headers=headers,params=params)

        if response.status_code == 200:
            print("Proceeding to extract the repos information")

            # decode the response 
            repos = json.loads(response.content.decode('utf-8'))
    
            # get the repos details of the organization
            repos_details = get_repos_retails(repos)
    
            repos_organization.append(repos_details)
    
            print(f"Repositories for {organization[i]} done !")
        else:
            print('Request Failed')
            
    return repos_organization