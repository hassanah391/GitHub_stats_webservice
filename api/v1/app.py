#!/usr/bin/python3
"""app.py to connect to API"""
import os
from api.v1.github_routes import app_views, cache
from flask import Flask, Blueprint, jsonify, make_response, render_template
from flask_cors import CORS

app = Flask(__name__)
app.config["CACHE_TYPE"] = "redis"
app.config["CACHE_REDIS_HOST"] = "localhost"
app.config["CACHE_REDIS_PORT"] = 6379
cache.init_app(app)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    host = os.getenv('GHSW_API_HOST', '0.0.0.0')
    port = int(os.getenv('GHSW_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
