from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class FlaskIndex(Resource):
    def get(self):
        return {'Flask': 'k8s'}

api.add_resource(FlaskIndex, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
