from flask import Flask

from app import route


def create_app():
    app = Flask(__name__)

    '''@app.route('/')
    def hello_world():
        return 'Hello, World!'''
    
     route.init_app(app)  

    return app
