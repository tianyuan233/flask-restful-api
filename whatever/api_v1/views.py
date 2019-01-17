from flask import Blueprint
from flask_restful import Api

from whatever.api_v1.resources import UserResource, UserList


blueprint = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
