from flask import Flask
from src.controllers import HelloController
from src.services import HelloService

hello_service = HelloService()
hello_controller = HelloController(hello_service)

app = Flask(__name__)

@app.route("/")
def sample_route():
    return hello_controller.get_hello()

app.run()