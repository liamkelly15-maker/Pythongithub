from github import Github

import os
access_token=os.environ.get("PAT")
# using an access token
#create the github api object from the imported class Github
g = Github(access_token)
for repo in g.get_user().get_repos():
   print(repo.name)

