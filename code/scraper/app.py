from flask import Flask, make_response, jsonify
import os
import sys

app = Flask(__name__)

app.secret_key = 'super_awesome_project'

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)


def main():
    configure()
    app.run(debug=True, port=7000)


def configure():
    print("Configuring Flask app:")

    register_blueprints()
    print("Registered blueprints")


def register_blueprints():
    from views import scraper_views

    app.register_blueprint(scraper_views.blueprint)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': error}), 404)


if __name__ == '__main__':
    main()
else:
    configure()
