from flask import Flask  # Import the Flask class from the flask module
import os  # Import the os module to work with file paths


def create_app():
    # Create a new Flask application instance
    app = Flask(__name__,
                template_folder=os.path.abspath('templates'),  # Specify the folder for HTML templates
                static_folder=os.path.abspath('static'))  # Specify the folder for static files (CSS, JS, images)

    # Load configuration settings from the config.py file
    app.config.from_object('config')

    # Import and register the main blueprint (a collection of routes) from the routes module
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Return the Flask application instance
    return app

