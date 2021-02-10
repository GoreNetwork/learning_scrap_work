from git import Repo
import os
from pprint import pprint


current_dir = os.getcwd()
repo = Repo(current_dir)
assert not repo.bare

thing = repo.commit
print (thing)
# pprint (dir(thing))
# for each in dir(thing):
#     if 'date'  in each:
#         print (each)

headcommit = repo.head.commit
commited_date = headcommit.authored_date
print (commited_date)

import time
# time.asctime(time.gmtime(headcommit.committed_date))
pprint (time.strftime("%a, %d %b %Y %H:%M", time.gmtime(commited_date)))

pprint (dir (repo.heads))

git = repo.git
git.checkout('test_branch')

