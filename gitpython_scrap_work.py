from git import Repo
import os
from pprint import pprint


current_dir = os.getcwd()
repo = Repo(current_dir)
# assert not repo.bare

# thing = repo.commit
# print (thing)
# pprint (dir(thing))
# for each in dir(thing):
#     if 'date'  in each:
#         print (each)

# tree = repo.heads.master.commit.tree

# assert len(tree.trees) > 0          # trees are subdirectories
# assert len(tree.blobs) > 0          # blobs are files
# assert len(tree.blobs) + len(tree.trees) == len(tree)

# for entry in tree:                                         # intuitive iteration of tree members
#     print(entry)

# assert repo.tree() == repo.head.commit.tree

headcommit = repo.head.commit
commited_date = headcommit.authored_date
print (commited_date)

import time
# time.asctime(time.gmtime(headcommit.committed_date))
pprint (time.strftime("%a, %d %b %Y %H:%M", time.gmtime(commited_date)))