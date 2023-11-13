import requests
import os
import json

#for listing a repo the auth is not required if repos are public

data = {"type": "all", "sort":"full_name", "direction": "asc"}

#username = input("Please enter your GitHub username: ")
username="liamkelly15-maker"
output = requests.get("https://api.github.com/users/{}/repos".format(username), data=json.dumps(data))
output = json.loads(output.text)

#print(output)

for reponame in output:
    print(reponame['name'])