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
     
     stillHaveCommits = True
     while stillHaveCommits:
     r = requests.get("http://{}:{}/cyclomatic".format(ipManager,portManager))
     json_data = json.loads(r.text)
        print(json_data)
        print("Received : {}".format(json_data['sha']))
        if json_data['sha'] == -2:  #  Manager waiting to start giving commits
           print("Manager waiting")
        else:
           if json_data['sha'] == -1:
                print("No items left")
                break
              subprocess.call(["bash", "workerGetCommit.sh", json_data['sha']])
              binRadonCCOutput = subprocess.check_output(["radon", "cc", "-s", "-a" , "workerData"])
              radonCCOutput = binRadonCCOutput.decode("utf-8")
           
           print(radonCCOutput)
           avgCCstartPos = radonCCOutput.rfind("(") # lookign for last bracket
           if radonCCOutput[avgCCstartPos+1:-2] == "": #no files left to calculate complexity
             print("No files")
             r = requests.post("http://{}:{}/cyclomatic".format(ipManager,portManager),json={'commitSha': json_data['sha'], 'complexity': -1})
        
        else:
          averageCC = float(radonCCOutput[avgCCstartPos+1:-2]) #get avg Cyclometric Complexity
          r = requests.post("http://{}:{}/cyclomatic".format(ipManager,portManager), json={'commitSha': json_data['sha'], 'complexity': averageCC})
       numCommitsDone += 1
       
if __name__ == '__main__':
      run()
