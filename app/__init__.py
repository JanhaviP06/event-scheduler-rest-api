from flask import Flask
from flask_sqlalchemy import SQLAlchemy #interact with db using python

#create database object globally
db=SQLAlchemy()

#appfactory
def create_app():
    app=Flask(__name__) 
     
    
    app.config['SECRET_KEY']='secret-key'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///events.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    #link db with app
    db.init_app(app)

     # Import and register routes
    from .routes import events_bp
    app.register_blueprint(events_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app