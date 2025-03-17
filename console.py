#!/usr/bin/python3
import cmd

import requests
from models.github_stats import GitHubStats
from flask import Flask, app
from api.v1.app import app
from api.v1.github_routes import cache

class GitHubStatsCLI(cmd.Cmd):
    intro = "Welcome to the GitHub Stats CLI. Type help or ? to list commands."
    prompt = "(github-stats) "

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_fetch_stats(self, arg):
        "Fetch GitHub stats for a user: fetch_stats <username>"
        if not arg:
            print("Please provide a username.")
            return
        stats = GitHubStats.get_user_stats(arg)
        print(stats)

    def do_fetch_repos(self, arg):
        "Fetch repositories for a user: fetch_repos <username>"
        if not arg:
            print("Please provide a username.")
            return
        repos = GitHubStats.get_user_repos(arg)
        print(repos)

    def do_fetch_languages(self, arg):
        "Fetch language breakdown for a user: fetch_languages <username>"
        if not arg:
            print("Please provide a username.")
            return
        languages = GitHubStats.get_language_breakdown(arg)
        print(languages)

    def do_clear_cache(self, arg):
        "Clear the API cache: clear_cache"
        print("Clearing cache...")
        with app.app_context():
            cache.clear()
        print("Cache cleared successfully.")

    def do_health_check(self, arg):
        """Check API health: health_check"""
    api_url = "http://localhost:5000/api/v1/github/health"
    print("Checking API health...")
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print("✅ API is healthy!")
        else:
            print(f"⚠️ API is reachable but returned status {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to reach API: {e}")

    def do_set_api(self, arg):
        "Set the API endpoint: set_api <url>"
        if not arg:
            print("Please provide an API URL.")
            return
        global API_URL
        API_URL = arg
        print(f"API endpoint set to {API_URL}")

    def do_exit(self, arg):
        "Exit the CLI: exit"
        print("Exiting GitHub Stats CLI.")
        return True

if __name__ == "__main__":
    GitHubStatsCLI().cmdloop()
