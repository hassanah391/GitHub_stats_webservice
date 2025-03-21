# API Directory

## Overview

The `api` directory contains the code for the web service that interacts with the GitHub API to provide various statistics about GitHub users. This includes fetching user information, repository details, language usage breakdowns, and star counts. The API is built using Flask and provides endpoints for accessing these statistics.

## API subdirectory structure
```
> tree
.
├── README.md
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-38.pyc
│   └── __init__.cpython-39.pyc
└── v1
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-38.pyc
    │   ├── __init__.cpython-39.pyc
    │   ├── app.cpython-38.pyc
    │   └── app.cpython-39.pyc
    ├── app.py
    ├── github_routes
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── __init__.cpython-39.pyc
    │   │   └── github_stats.cpython-38.pyc
    │   └── github_stats.py
    └── templates
        └── index.html

6 directories, 16 files
```
## Files

### `v1/`

This directory contains the version 1 of the API implementation.

#### `app.py`

This file initializes the Flask application, sets up the Redis cache, and registers the API blueprints. It also defines the root route to render the index page.

#### `github_routes/`

This directory contains the route definitions for the GitHub statistics API.

##### `github_stats.py`

This file defines the endpoints for fetching GitHub user statistics, repositories, and language breakdowns. It also includes a health check endpoint.

##### `__init__.py`

This file initializes the Blueprint for the GitHub routes and sets up the cache.

#### `templates/`

This directory contains the HTML templates for the web interface.

##### `index.html`

This file defines the HTML structure and styling for the web interface where users can enter a GitHub username and view the statistics.

### `__init__.py`

This is an empty file that indicates that the `api` directory is a Python package.

## Usage

To run the Flask application, use the following command:

```sh
python3 api/v1/app.py
```

You can then access the web interface by navigating to `http://localhost:5000` in your web browser.

## Environment Variables

The Flask application relies on several environment variables for configuration:

- `GITHUB_PAT`: Your GitHub Personal Access Token for authenticated requests
- `CACHE_REDIS_URL`: The Redis URL for caching

## Dependencies

The API depends on several Python packages. Make sure to install the required packages:

```sh
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.