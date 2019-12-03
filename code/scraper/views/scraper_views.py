from typing import Optional

import bson
import bson.json_util
import json
from flask import render_template, Blueprint, redirect, session, jsonify, request

from infrastructure.scraping_poc import Scraper

blueprint = Blueprint('account', __name__, template_folder='templates')

@blueprint.route('/scraper/get_courses', methods=['POST'])
def get_courses():
    scraper = Scraper()

    return jsonify(scraper.scrap())