from github import Github

import os
access_token=os.environ.get("PAT")
# using an access token
#create the github api object from the imported class Github
g = Github(access_token)

#look up the python github library at https://pygithub.readthedocs.io/en/stable/

