from flask import Flask, render_template
import os
import sys

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


def register_blueprints():
    from views import home_views
    from views import account_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(account_views.blueprint)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error/404.html', vm=None)


if __name__ == '__main__':
    main()
else:
    configure()
