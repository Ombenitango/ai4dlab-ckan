from flask import Blueprint


ai4dlab = Blueprint(
    "ai4dlab", __name__)


def page():
    return "Hello, ai4dlab!"


ai4dlab.add_url_rule(
    "/ai4dlab/page", view_func=page)


def get_blueprints():
    return [ai4dlab]
