from flask import Flask
from .resume.routes import resume
from .admin.routes import admin
from .gallery.routes import gallery

def create_app():
    app = Flask(__name__)

    app.register_blueprint(resume)
    app.register_blueprint(admin)
    app.register_blueprint(gallery)
    return app
