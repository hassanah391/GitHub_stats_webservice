#!/usr/bin/python3
"""app.py to connect to API"""
import os
from api.v1.github_routes import app_views, cache  # Import routes and cache from the application
from flask import Flask, Blueprint, jsonify, make_response, render_template  # Flask framework and utilities
from flask_cors import CORS  # For handling Cross-Origin Resource Sharing (CORS)

# Initialize Flask application
app = Flask(__name__)

# Configure caching with Redis
app.config["CACHE_TYPE"] = "redis"  # Specify Redis as the cache type
app.config["CACHE_REDIS_HOST"] = "localhost"  # Redis host
app.config["CACHE_REDIS_PORT"] = 6379  # Redis port
app.config["CACHE_REDIS_URL"] = "redis://default:ObPZZQhQfOyVFBGFQbNJSRORRVJoACAh@redis.railway.internal:6379"  # Redis connection URL

# Initialize cache with the app
cache.init_app(app)

# Register the blueprint for application routes
app.register_blueprint(app_views)

# Enable CORS for all routes, allowing requests from any origin
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})

# Define a custom error handler for 404 errors
@app.errorhandler(404)
def page_not_found(error):
    """Return a JSON response with a 404 status code"""
    return make_response(jsonify({'error': 'Not found'}), 404)

# Define the root route
@app.route("/")
def index():
    """Render the index.html template"""
    return render_template("index.html")

# Entry point of the application
if __name__ == "__main__":
    # Get the host and port from environment variables, with defaults
    host = os.getenv('GHSW_API_HOST', '0.0.0.0')
    port = int(os.getenv('GHSW_API_PORT', '5000'))
    
    # Run the Flask application
    app.run(host=host, port=port, threaded=True)
