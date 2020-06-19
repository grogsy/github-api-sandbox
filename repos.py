import requests
import json
import base64

def get_file_from_repo(repo_name, owner_name, file_path):
    '''
    return the contents of a file from a repo hosted on github
    '''
    api_url = f'https://api.github.com/repos/{owner_name}/{repo_name}/contents/{file_path}'

    res = requests.get(api_url)
    json_from_bytes = json.loads(res.content)
    file_contents = base64.b64decode(json_from_bytes['content'])

    try:
        file_contents = file_contents.decode('utf-8')
    except (UnicodeDecodeError, AttributeError):
        pass

    return file_contents

print(get_file_from_repo(repo_name='ogpp', owner_name='grogsy', file_path='config.py'))

# get a file from repo subdirectory
print(get_file_from_repo(repo_name='ogpp', owner_name='grogsy', file_path='ogpp/routes/summoner.py'))