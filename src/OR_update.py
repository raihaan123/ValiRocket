# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:02:40 2020

@author: Raihaan
"""

# Additional libraries
from globalV import git_user, token, repo
import first_push
import os

print("Running first push...")

try:
    first_push.fpush()

except Exception:
    print("Rocket file already exists")


# Pushing the updated parsed file
print(os.system("git config --local user.email \"action@github.com\""))
print(os.system("git config --local user.name \"github-actions\""))
print(os.system("git checkout -b Production"))
print(os.system("git add --all"))
print(os.system("git commit -m \"ValiRocket sync\" -a"))
print(os.system(f"git push https://{token}@github.com/{git_user}/{repo}.git"))