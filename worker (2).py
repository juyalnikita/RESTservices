# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:23:06 2017

@author: Nikita Juyal
"""

import requests,json,subprocess
 
def run():
     ipManager = input('Enter IP of Manager')
     portManager = input('Enter port of Manager')
     
     #Repo not pulled yet
     r = requests.get("http://{}:{}/repo".format(ipManager,portManager),json = {'pullStatus' : False})
     json_data = json.loads(r.text)
     repoUrl = json_data['repo']
     subprocess.call(["bash", "workerInitScript.sh", repoUrl])
     
     #Repo pulled
     r = requests.get("http://{}:{}/repo".format(ipManager,portManager),json = {'pullStatus' : True})
     
     
     #add code for multiple commits
       
if __name__ == '__main__':
      run()