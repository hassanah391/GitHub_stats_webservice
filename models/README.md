# Models Directory

## Overview

The `models` directory contains the core logic for interacting with the GitHub API and retrieving various statistics about GitHub users. This includes fetching user information, repository details, language usage breakdowns, and star counts.

## Model subdirectory structure
```
> tree
.
├── README.md
├── __init__.py
└── github_stats.py

0 directories, 3 files
```
## Files

### `github_stats.py`

This file defines the `GitHubStats` class, which provides methods to interact with the GitHub API and retrieve statistics. The main functionalities include:

- Fetching user profile data (name, bio, location, etc.)
- Calculating total stars across all repositories
- Listing all repositories with their details
- Generating language usage statistics as percentages
- Handling GitHub API pagination automatically
- Managing API rate limiting with appropriate error responses

### `__init__.py`

This is an empty file that indicates that the `models` directory is a Python package.

## Usage

To use the `GitHubStats` class, you can import it into your project and call its static methods. Here is an example:

```python
from models.github_stats import GitHubStats

# Get basic user information
user_data = GitHubStats.get_user_stats("username")

# Get language breakdown
languages = GitHubStats.get_language_breakdown("username")
```

## Environment Variables

The `GitHubStats` class relies on a GitHub Personal Access Token (PAT) for authenticated requests. You need to set the `GITHUB_PAT` environment variable with your token:

```sh
export GITHUB_PAT=your_github_pat
```

## Dependencies

The `github_stats.py` file depends on the `requests` library for making HTTP requests to the GitHub API. Make sure to install the required packages:

```sh
pip install requests
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.