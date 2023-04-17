from flask import jsonify
from ..services import HelloService

class HelloController:
    def __init__(self, hello_service: HelloService):
        self.hello_service = hello_service

    def get_hello(self):
        result = self.hello_service.get_one()
        return jsonify(result.serialize())