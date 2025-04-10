"""
Utility functions for integrating with GitHub API to fetch repositories and project data.
"""

import requests
from django.conf import settings

def fetch_github_repos(username):
    """
    Fetch all public repositories for a GitHub username using the GitHub API.
    Uses the API token from settings/secrets if available for increased rate limits.
    
    Args:
        username (str): GitHub username to fetch repositories for
        
    Returns:
        list: List of repository dictionaries or empty list if request fails
    """
    url = f'https://api.github.com/users/{username}/repos'
    
    # Use API token from settings if available
    headers = {}
    if hasattr(settings, 'GITHUB_API_KEY') and settings.GITHUB_API_KEY:
        headers['Authorization'] = f'token {settings.GITHUB_API_KEY}'
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"GitHub API error: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching GitHub repositories: {e}")
        return []

def get_repo_details(username, repo_name):
    """
    Get detailed information about a specific repository.
    
    Args:
        username (str): GitHub username
        repo_name (str): Repository name
        
    Returns:
        dict: Repository details or None if request fails
    """
    url = f'https://api.github.com/repos/{username}/{repo_name}'
    
    # Use API token from settings if available
    headers = {}
    if hasattr(settings, 'GITHUB_API_KEY') and settings.GITHUB_API_KEY:
        headers['Authorization'] = f'token {settings.GITHUB_API_KEY}'
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception:
        return None