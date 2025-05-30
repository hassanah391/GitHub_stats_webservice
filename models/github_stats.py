#!/usr/bin/python3
"""
GitHub Statistics API Module

This module provides a class to interact with the GitHub API
and retrieve various statistics about GitHub users.
"""
import os
import requests


class GitHubStats:
    """GitHub Stats"""
    # Get the GitHub token from environment variables
    GITHUB_PAT = os.getenv("GITHUB_PAT")

    BASE_URL = "https://api.github.com"

    @staticmethod
    def get_total_stars(username):
        """Returns the total stars of a given user, handling pagination"""
        total_stars = 0
        page = 1

        while True:
            url = (
                f"{GitHubStats.BASE_URL}/users/{username}/repos"
                f"?per_page=100&page={page}"
            )

            headers = {
                "User-Agent": "GitHubStatsApp",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            }

            if GitHubStats.GITHUB_PAT:
                headers["Authorization"] = f"token {GitHubStats.GITHUB_PAT}"
            response = requests.get(url, headers=headers)

            if (
                response.status_code == 403
                and "X-RateLimit-Remaining" in response.headers
            ):
                return {
                    "error": "GitHub API rate limit exceeded.Try again later."
                }

            if response.status_code != 200:
                return 0  # Return 0 if request fails

            repos = response.json()
            if not repos:
                break  # Stop when there are no more repos

            total_stars += sum(
                repo.get("stargazers_count", 0) for repo in repos
            )
            page += 1  # Move to the next page

        return total_stars

    @staticmethod
    def get_user_stats(username):
        """Fetches GitHub statistics for a given username."""
        url = f"{GitHubStats.BASE_URL}/users/{username}"
        headers = {
            "User-Agent": "GitHubStatsApp",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if GitHubStats.GITHUB_PAT:
            headers["Authorization"] = f"token {GitHubStats.GITHUB_PAT}"
        response = requests.get(url, headers=headers)

        if (
            response.status_code == 403
            and "X-RateLimit-Remaining" in response.headers
        ):
            return {
                "error": "GitHub API rate limit exceeded. Try again later."
            }

        if response.status_code != 200:
            return {
                "error": "Failed to fetch user data",
                "status_code": response.status_code
            }

        desired_data = [
            "name", "bio", "location", "public_repos",
            "followers", "following", "avatar_url"
        ]
        user_data = response.json()

        stats = {key: user_data.get(key) for key in desired_data}
        stats["total_stars"] = GitHubStats.get_total_stars(username)

        return stats

    @staticmethod
    def get_user_repos(username):
        """Retrieves a list of repos for a given username."""
        repos_list = []
        page = 1
        headers = {
            "User-Agent": "GitHubStatsApp",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if GitHubStats.GITHUB_PAT:
            headers["Authorization"] = f"token {GitHubStats.GITHUB_PAT}"

        while True:
            url = (
                f"{GitHubStats.BASE_URL}/users/{username}/repos"
                f"?per_page=100&page={page}"
            )
            response = requests.get(url, headers=headers)

            if response.status_code == 403:
                if response.headers.get("X-RateLimit-Remaining") == "0":
                    return {
                        "error": (
                            "GitHub API rate limit exceeded. "
                            "Try again later."
                        )
                    }

            if response.status_code != 200:
                return {
                    "error": "Failed to fetch user data",
                    "status_code": response.status_code
                }

            repos = response.json()
            if not repos:
                break  # Stop if no more repos

            repos_list.extend([
                {
                    "name": repo.get("name"),
                    "language": repo.get("language"),
                    "stars": repo.get("stargazers_count", 0),
                    "forks": repo.get("forks_count", 0)
                }
                for repo in repos
            ])

            page += 1  # Move to the next page

        return repos_list

    @staticmethod
    def get_language_breakdown(username):
        """Calculates the percentage usage of different programming languages."""
        user_languages = {}
        repos = GitHubStats.get_user_repos(username)

        # Handle errors from get_user_repos
        if isinstance(repos, dict) and "error" in repos:
            return repos  # Return the error message from get_user_repos

        headers = {
            "User-Agent": "GitHubStatsApp",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if GitHubStats.GITHUB_PAT:
            headers["Authorization"] = f"token {GitHubStats.GITHUB_PAT}"
        total_bytes = 0

        for repo in repos:
            repo_name = repo["name"]
            url = (
                f"{GitHubStats.BASE_URL}/repos/{username}"
                f"/{repo_name}/languages"
            )
            response = requests.get(url, headers=headers)

            # Handle rate limit exceeded
            if (
                response.status_code == 403
                and response.headers.get("X-RateLimit-Remaining") == "0"
            ):
                return {
                    "error": "GitHub API rate limit exceeded. Try again later."
                }

            # Skip this repo if request fails
            if response.status_code != 200:
                continue

            languages_repo = response.json()  # Fetch languages for the repo

            # Aggregate language bytes
            for language, bytes_used in languages_repo.items():
                user_languages[language] = (
                    user_languages.get(language, 0) + bytes_used
                )
                total_bytes += bytes_used  # Accumulate total bytes here

        # Convert raw byte counts to percentages
        if total_bytes == 0:
            return {}  # Avoid division by zero

        return {
            language: round((bytes_used / total_bytes) * 100, 2)
            for language, bytes_used in user_languages.items()
        }

    @staticmethod
    def check_auth():
        """Check if the GitHub token is being used correctly."""
        url = "https://api.github.com/users/hassanah391"
        headers = {
            "User-Agent": "GitHubStatsApp",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if GitHubStats.GITHUB_PAT:
            headers["Authorization"] = f"token {GitHubStats.GITHUB_PAT}"

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print("✅ Authentication successful!")
            print("Authenticated as:", response.json().get("login"))
        elif response.status_code == 401:
            print("❌ Authentication failed! Check your GitHub token.")
        else:
            print(
                f"⚠️ Unexpected response: {response.status_code}",
                response.json()
            )

    @staticmethod
    def check_rate_limit():
        """Checks Remaining Requests"""
        url = "https://api.github.com/rate_limit"
        headers = {
            "User-Agent": "GitHubStatsApp",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if GitHubStats.GITHUB_PAT:
            headers["Authorization"] = f"token {GitHubStats.GITHUB_PAT}"

        response = requests.get(url, headers=headers)
        data = response.json()

        if "rate" in data:
            print(
                f"✅ Authenticated! Remaining Requests: {data['rate']['remaining']}"
            )
        else:
            print("❌ Authentication Failed!")
