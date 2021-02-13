# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:02:40 2020

@author: Raihaan
"""

# Additional libraries
import valispace
from flask import Flask, render_template, request, redirect, jsonify
#from testing import *
import os
import globalV
import XPath
from threading import Thread

# Instantiate a Flask server
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/sign_in', methods=['GET','POST'])
def login():
    
    if request.method == "POST":
        
        user = request.form['uname']
        passwd = request.form['psw']
        
        globalV.vs = valispace.API(url='iclrocketry.valispace.com', username = user, password = passwd)
        #valispaceObj = valispace.API(url='iclrocketry.valispace.com', username = user, password = passwd)
        
        return redirect('/success')
    return render_template("login.html")


@app.route('/success')    
def success():
    
        project_name = 'Sporadic_Impulse_COTS2020'

        project = {'name':project_name, 'id':globalV.vs.get_project_by_name(name=project_name)[0]['id']}
        message = "Currently working on the "+project['name']+" project (ID: "+str(project['id'])+")"
        
        # Run the initial push routine
        url = 'https://raw.githubusercontent.com/icl-rocketry/The-Complete-Final-Absolute-Sporadic-Impusle/master/The_Sporadic_Impulse_COTS.rkt'
        
        
        thread = Thread(target=XPath.unpack, args=(int(project['id']), url, globalV.vs))
        thread.daemon = True
        thread.start()
        # return jsonify({'thread_name': str(thread.name),
        #                 'started': True})
    
        return render_template("response.html", message = message, response1 = "This will look nicer...", response2 = "Things are happing in Valispace rn, go check it out!")
        
        
        #XPath.unpack(project=int(project['id']), url=url, vs=globalV.vs)
        
        # Testing code - remove!
        # response1 = testComponent(project, vs)
        
        # try:
        #     response2 = testVali(vs, int(response1['id']))
        # except Exception as exc:
        #     response2 = "Weep... " + str(exc)
            
        
        #return render_template("response.html", message = message, response1 = "Success!", response2 = "Lol")

    

# @app.route('/rest/OR', methods=['GET','POST'])
# def listen():
    
#     if request.method == "POST":
        
        




# Start webserver on PaaS provider
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)