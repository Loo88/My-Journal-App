from flask import Flask
from app.routes import routes
from app.error_handlers import register_error_handlers

def create_app():
    app = Flask(__name__)
    
    #register routes and error handlers
    routes(app) #pass the app instance to the routes function
    
    #register error handlers
    register_error_handlers(app)

    return app
