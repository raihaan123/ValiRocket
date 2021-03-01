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
    os.system("git checkout -b Production")
    first_push.fpush()

    # Pushing the updated parsed file
    os.system("git config --local user.email \"action@github.com\"")
    os.system("git config --local user.name \"github-actions\"")
    os.system("git add --all")
    os.system("git commit -m \"ValiRocket sync\" -a")
    os.system(f"git push https://{token}@github.com/{git_user}/{repo}.git")

except Exception:
    print("Rocket file already exists")
