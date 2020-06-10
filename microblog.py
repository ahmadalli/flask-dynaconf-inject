from flask import Flask
from dynaconf import FlaskDynaconf
from flask_injector import FlaskInjector

app = Flask(__name__)
FlaskDynaconf(app)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

def configure(binder):
    pass

FlaskInjector(app=app, modules=[configure])
