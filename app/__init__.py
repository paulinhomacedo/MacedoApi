from flask import Flask


def create_app():
    app = Flask(__name__)
    
    from app import route

    route.init_app(app)   

    return app
