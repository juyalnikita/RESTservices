from flask import Flask
from flask_restful import Resource, Api, reqparse
import json, requests, time, getpass

flask = Flask(__name__)
api = Api(app)


class getReposit(Resource)
    def __init__(self):
        global managerS 
        self.server = managerS #initialise the global server
        super(getRepository, self).__init__()
        self.reqparser = reqparse.RequestParser()
    
        self.reqparser.add_argument('pullStatus', type=int, location = 'json')
        self.reqparser.add_argument('complexity', type=float, location='json')
    
    def get(self):
        args = self.reqparser.parse_args()
        if args['pullStatus'] == False: #Repo has not been pulled- no action needed
            return {'repo': "https://github.com/juyalnikita/scchatbot"}
        if args['pullStatus'] == True:
            self.server.curWorkerNo += 1 #Repo was pulled, current worker no. can be incremented
            if self.server.curWorkerNo == self.server.numWorkers: #Check if all workers have pulled Repo
                self.server.startTime = time.time() #Timer started
            print("WORKER NUMBER: {}".format(self.server.curWorkerNo))
        
    def post(self): 
        pass # not needed because slave/worker won't post anything in getRepo clas
api.add_resource(getRepository, "/repo", endpoint="repo")
    
    
class cyclomaticApi() #to obtain commits and post cyclometric complexity results
def __init__(self):
    global managerS 
    self.server = managerS #initialise the global server

    
class manager():
     def __init__(self):
         self.numWorkers = input("Enter number of workers: ")
         self.numWorkers = int(self.numWorkers)
         self.curWorkerNo = 0 #No. of workers who are connected to manager
         self.startTime = 0.0
         
         gitUsername = input("Type the Github username to use authenticated requests, or return to use unauthenticated requests:")
         print(len(gitUsername))
         if len(gitUsername) != 0:
            gitPassword = getpass.getpass("Type your Github password: ")
         morePages = True  # Loop control variable to check if more pages on github API
         currentPage = 1
         self.commitList = [] # buildinglist containing sha values from repo
         while morePages:
                if len(gitUsername) == 0:
                    r = requests.get("https://api.github.com/repos/juyalnikita/scchatbot/commits?page={}&per_page=100".format(currentPage))
                else
                    r = requests.get("https://api.github.com/repos/juyalnikita/scchatbot/commits?page={}&per_page=100".format(currentPage), auth=(gitUsername, gitPassword))
                json_data = json.loads(r.text)
                if len(json_data) < 2:
                    morePages = False
                    print("All pages iterated")
                else:
                    for x in json_data:
                        self.commitList.append(x['sha']) # sha commit
                        print("Commit sha: {}".format(x['sha']))
                        print("\n")
                        currentPage += 1 #page increment after sha commit
          self.totalNumberOfCommits = len(self.commitList)  
          print("Number of commits: {}".format(self.totalNumberOfCommits))

if __name__ == "__main__":
    managerS = manager()  # initialise instance of managerServer()
    flask.run(port=5000) 
