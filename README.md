# GitHub Stats Webservice

## Project Overview

The GitHub Stats Webservice is a web application that provides various statistics about GitHub users. It interacts with the GitHub API to fetch user information, repository details, language usage breakdowns, and star counts. The application offers a user-friendly interface to display these statistics and provides a command-line interface (CLI) for advanced users.

![GitHub Stats Webservice](/assets/homepage.png)


## Features

- Fetch user profile data (name, bio, location, etc.)
- Calculate total stars across all repositories
- List all repositories with their details
- Generate language usage statistics as percentages
- Handle GitHub API pagination automatically
- Manage API rate limiting with appropriate error responses


## Deployment

### Deploying on Railway

The GitHub Stats Webservice is deployed on Railway. You can access the live application using the following link:

[GitHub Stats Webservice on Railway](https://githubstatswebservice-production.up.railway.app/)

## Environment Setup

### Prerequisites

- Python 3.7+
- Redis server (for caching)
- GitHub Personal Access Token (PAT) for authenticated requests

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/hassanah391/GitHub_stats_webservice.git
    cd GitHub_stats_webservice
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add your GitHub PAT for better performance:

    ```sh
    GITHUB_PAT=your_github_pat
    ```

5. **Start the Redis server:**

    ```sh
    redis-server
    ```

## Running the Application

### Web Interface

1. **Start the Flask application:**

    ```sh
    python3 api/v1/app.py
    ```

2. **Access the web interface:**

    Open your web browser and navigate to `http://localhost:5000`.

### Command-Line Interface (CLI)

1. **Run the CLI:**

    ```sh
    python3 console.py
    ```

2. **Available CLI commands:**

    - `fetch_stats <username>`: Fetch GitHub stats for a user
    - `fetch_repos <username>`: Fetch repositories for a user
    - `fetch_languages <username>`: Fetch language breakdown for a user
    - `clear_cache`: Clear the API cache
    - `health_check`: Check API health
    - `set_api <url>`: Set the API endpoint
    - `quit` or `exit`: Exit the CLI

## Project Structure
``` 
> tree
.
├── Procfile
├── README.md
├── __pycache__
│   ├── app.cpython-38.pyc
│   └── app.cpython-39.pyc
├── api
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   └── __init__.cpython-39.pyc
│   └── v1
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-38.pyc
│       │   ├── __init__.cpython-39.pyc
│       │   ├── app.cpython-38.pyc
│       │   └── app.cpython-39.pyc
│       ├── app.py
│       ├── github_routes
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   │   ├── __init__.cpython-38.pyc
│       │   │   ├── __init__.cpython-39.pyc
│       │   │   └── github_stats.cpython-38.pyc
│       │   └── github_stats.py
│       └── templates
│           └── index.html
├── console.py
├── models
│   ├── README.md
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   └── github_stats.cpython-38.pyc
│   └── github_stats.py
└── requirements.txt

10 directories, 26 files
```


## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.