from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"Sateswar":{"age": 19,"gender": "male"},
         "Aashutosh":{"age": 18,"gender": "male"}
         }

class HelloWorld(Resource):
    def get(self):
        return {"data":"Hello World"}
     
    def get(self,name,test):
        return {"name":name, "test":test}
    
    def get(self,name):
        return names[name]
    
    def post(self):
        return {"data":"Post Hello World"}

api.add_resource(HelloWorld,"/helloworld/<string:name>")


videos={}
class Video(Resource):
    def get(self,video_id):
        return videos[video_id]
    

    def put(self,video_id):
        print(request.form['likes'])
        return {}
api.add_resource(HelloWorld,"/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)


