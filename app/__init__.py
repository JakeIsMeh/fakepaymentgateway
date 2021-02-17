import os

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['ENDPOINT'] = 'http://localhost:5000/transaction/recv'

    if not os.path.exists('instance'): os.mkdir('instance')

    from . import api
    from . import dash

    app.register_blueprint(api.bp)
    app.register_blueprint(dash.bp)

    return app