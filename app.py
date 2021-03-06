from flask import Flask, request
from flask_restful import Resource, Api

from flask_cors import CORS, cross_origin
from flask import jsonify

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/": {"origins": "*"}})

ROBOT_NAME = "macbook"
ROS_VERSION = "jade"

class Robot(Resource):

    @cross_origin(origin="*", headers=["content-type", "autorization"])
    def get(self):
        return jsonify({'name': ROBOT_NAME,
        'ros': ROS_VERSION,
        'hardware': 'macbook',
	'message': 'hi, i am '+'ROBOT_NAME',
        'ros_packages': ['rosserial', 'rosbridge']})

class Roscore(Resource):

    decorators = [cross_origin(origin="*", headers=["content-type", "autorization"])]

    def get(self):
        return jsonify({'response': 'get roscore ok'})
    def post(self):
        return jsonify({'response': 'post roscore ok'})
    def put(self):
        return jsonify({'response': 'put roscore ok'})

class Rosfile(Resource):

    decorators = [cross_origin(origin="*", headers=["content-type", "autorization"])]

    def post(self):
	json_data = request.get_json(force=True)
	filecontent = json_data["filecontent"]
        print (filecontent)
	filename = json_data["filename"]
	print (filename)
        return jsonify({'response': 'ok'})
    def put(self):
        return jsonify({'response': 'ok'})

class Rosnode(Resource):

    decorators = [cross_origin(origin="*", headers=["content-type", "autorization"])]

    def post(self):
    	json_data = request.get_json(force=True)
    	node = json_data["node"]
    	files = json_data["files"]
    	print(node)
    	print (files)
        return jsonify({'response': 'node uploaded ok'})
    def put(self):
	return jsonify({'response': 'ok'})

class RosKill(Resource):

    decorators = [cross_origin(origin="*", headers=["content-type", "autorization"])]

    def post(self):
	json_data = request.get_json(force=True)
	print ("killing Node " +str(json_data["nodeId"]))
        return jsonify({'response': 'killed ok'})

class GetCoreAddress(Resource):

	decorators = [cross_origin(origin="*", headers=["content-type", "autorization"])]

	def post(self):
		json_data = request.get_json(force=True)
		print ("received core is active on" + json_data["coreAddress"])
		return "ok"

api.add_resource(GetCoreAddress, '/getCoreAddress')
api.add_resource(RosKill, '/roskill')
api.add_resource(Rosnode, '/rosnode')
api.add_resource(Rosfile, '/rosfile')
api.add_resource(Robot, '/discovery')
api.add_resource(Roscore, '/roscore')

@app.route('/')
def index():
    return "Hello"

@app.route('/old_discovery')
@cross_origin(origin="*", headers=["content-type", "autorization"])
def disc():
    return jsonify({'name': ROBOT_NAME, 'ros': ROS_VERSION, 'hardware': 'macbook', 'ros_packages': ['rosserial', 'rosbridge']})



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
