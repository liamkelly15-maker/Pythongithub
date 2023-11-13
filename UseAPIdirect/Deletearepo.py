import requests
import os
import json
import runpy

token = os.environ.get("PAT")
print(token)
reponame = input("Please enter the repo name you want to delete : ")

GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}

username="liamkelly15-maker"
#username = input("Please enter your GitHub username: ")
r = requests.delete("https://api.github.com/repos/{}/{}".format(username, reponame), headers=headers)
print(r)

#now call the listrepo.py to confirm deletion
runpy.run_path(path_name='listarepo.py')
