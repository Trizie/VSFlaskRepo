from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
DB_NAME = os.getenv("DB_NAME")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # delete before uploading to pythonanywhere

# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle' : 280}
db.init_app(app)

def create_app():

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Lebensmittel
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
