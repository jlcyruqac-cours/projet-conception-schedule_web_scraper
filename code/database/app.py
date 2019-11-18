from flask import Flask, render_template
import os
import sys

from database.models import mongo_setup
from database.models.users import User

app = Flask(__name__)

app.secret_key = 'super_awesome_project'

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)


def main():
    configure()
    app.run(debug=True)


def configure():
    print("Configuring Flask app:")

    register_blueprints()
    print("Registered blueprints")

    setup_db()

def setup_db():
    mongo_setup.global_init()

def register_blueprints():
    from views import database_views

    app.register_blueprint(database_views.blueprint)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error/404.html', vm=None)


if __name__ == '__main__':
    main()
else:
    configure()
