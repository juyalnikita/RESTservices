from flask import Flask
from flask_restful import Resource, Api

flask = Flask(__name__)
api = Api(app)

class getReposit(Resource)
def __init__(self):
    global managerS 
    self.server = managerS #initialise the global server


class cyclomaticApi() #to obtain commits and post cyclometric complexity results
def __init__(self):
    global managerS 
    self.server = managerS #initialise the global server

#class manager(): to be defined

if __name__ == "__main__":
    managerS = manager()  # initialise instance of managerServer()
    app.run(port=5000) 
