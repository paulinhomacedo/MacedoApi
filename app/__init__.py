from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    
    '''from app import route

    route.init_app(app) '''  

    return app
