# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:02:40 2020

@author: Raihaan
"""

# Additional libraries
import first_push

print("Running first push...")

try:
    first_push.fpush()
except Exception:
    print("Rocket file already exists")
