from flask import Blueprint, jsonify


healthcheck = Blueprint("healthcheck", __name__)


@healthcheck.route("/")
def home():
    return jsonify({'message': 'success'})
