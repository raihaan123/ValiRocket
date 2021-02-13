# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:42:49 2020

@author: Raihaan
"""

# XPath stuff in here

import xml.etree.ElementTree as ET
from classes import component, vali, textvali
import urllib
#from uwsgidecorators import thread

# Initialise the XML structure, push the main component

def unpack(project, url, vs):
    
    tree = ET.parse(urllib.request.urlopen(url, data=None,))
    root = tree.getroot()[1][0]
    
    # Adjusting the names
    for components in root.iter('Name'):
        components.text = components.text.replace(" ", "_")
    
    rocket = component([i.text for i in root.iter('Name')][0], "null", project)
    parent = rocket.push(vs)

    # Ready for pushing to Valispace
    for child in root[27]:
        pusher(child, parent, project, vs)
    


def pusher(child, parent, project, vs):
    subparts = 0
    name = child.findall('Name')[0]
    child.tag = name.text
    child.remove(name)

    #DEBUG
    #print(child.tag)
    
    # Instantiate the component object
    comp = component(child.tag, parent, project)
    uid = comp.push(vs)
    
    for baby in child:
        
        if baby.tag == "AttachedParts":
            baby.text = None
            
            try:
                baby[0]
                subparts = 1
                temp = baby
                
            except IndexError:
                None
                
            continue
        
        try:
            value = float(baby.text)
            val = vali(baby.tag, uid, value)
        
        except ValueError:
            val = textvali(baby.tag, uid, baby.text)
            
        except TypeError:
            val = textvali(baby.tag, uid, "Not defined")
        
        val.push(vs)
    
    if subparts == 1:
        for i in range(0, len(temp)):
            
            pusher(temp[i], uid, project, vs)


# BOOM
#unpack(project=28)


    
    # subparts = 0
    # name = child.findall('Name')[0]
    # child.tag = name.text
    # child.remove(name)

    # print(child.tag)
    
    # for baby in child:
    #     if baby.tag == "AttachedParts":
    #         subparts = 1
    #         temp = baby
    #         continue
        
    #     print("   "+baby.tag+" = "+baby.text)
        
    # #Subpart declerations here

    # print(temp.tag)
        
    
#[child for child in [kid for kid in root.iter('AttachedParts')]]