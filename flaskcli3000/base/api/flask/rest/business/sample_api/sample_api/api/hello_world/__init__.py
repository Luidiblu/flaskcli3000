
from flask_restplus import Resource
from flask import request  # noqa
from ...api import api, parser_auth
from .helper import HelloWorldHelper

ns = api.namespace('hello-world', description='Hello world, i am alive')


@ns.route('')
class HelloWorldRoute(Resource):

    @ns.expect(parser_auth, validate=True)
    def get(self):
        return HelloWorldHelper.resolve_hello_world(), 200