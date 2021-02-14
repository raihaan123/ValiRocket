# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:02:40 2020

@author: Raihaan
"""

# Additional libraries
import sys
import os
import valispace
import globalV
import XPath


user = "raihaan.usman19"
# passwd = str(sys.argv)
print(os.getenv('INPUT_TEST_VAR'))

# print("Connecting to Valispace...")
# globalV.vs = valispace.API(url='iclrocketry.valispace.com',
#                             username=user, password=passwd)
# print("Connected!")

# print("Running XPath...")
# globalV.project_id = globalV.vs.get_project_by_name(name=globalV.project_name)[0]['id']

# try:
#     XPath.unpack(int(globalV.project_id), globalV.file, globalV.vs)
# except:
#     print("Rocket file already exists")
