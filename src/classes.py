# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:54:48 2020

@author: Raihaan
"""

# Component API call class
class component:
    
    def __init__(self, name, parent, project):
        
        self.name    = name
        self.parent  = parent
        self.project = project
    
    def push(self, valispace):
        
        valispace.post_data(type='component', data="""{
            "name": \"""" + self.name + """\",
            "parent": """ + str(self.parent) + """,
            "project": """ + str(self.project) + """,
            "tags": [
              9
            ]
        }""")
            
        return(valispace.get_component_by_name(unique_name = self.name, project_name = "Sporadic_Impulse_COTS2020")['id'])

        

# Vali API call class
class vali:
    
    def __init__(self, name, parent, value):
        
        self.parent = str(parent)
        self.name   = name
        self.value  = str(value)
    
    def push(self, valispace):
        
        valispace.post_data(type='vali', data="""{
            "shortname": \"""" + self.name + """\",
            "formula": """ + self.value + """,
            "parent": """ + self.parent + """,
            "tags": [
              9
            ]
        }""")
            
class textvali:
    
    def __init__(self, name, parent, text):
        
        self.parent = str(parent)
        self.name   = name
        self.text  = text
    
    def push(self, valispace):
        
        valispace.post_data(type='textvali', data="""{
            "shortname": \"""" + self.name + """\",
            "text": \"""" + self.text + """\",
            "parent": """ + self.parent + """,
            "tags": [
              9
            ]
        }""")