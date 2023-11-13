import os
import json
import requests

#get a github access token and assign to env var
#set-item -path env:PAT -Value <token>


token = os.environ.get("PAT")

#One more time let’s go to the GitHub documentation
#https://docs.github.com/en/rest/reference/repos

###get the option for creating a public or private repo


reponame = input("Please enter the repo name you want to create : ")
GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}

r = requests.post(GITHUB_API_URL +"user/repos" + "", data=json.dumps(data), headers=headers)
#add a change
