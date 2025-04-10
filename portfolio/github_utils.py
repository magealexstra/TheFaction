"""
Utility functions for integrating with GitHub API to fetch repositories and project data.

Currently placeholders. Requires 'requests' or 'PyGithub' package.

Example using requests:
---------------------------------
import requests

def fetch_github_repos(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

# Usage:
# repos = fetch_github_repos('magealexstra')
# for repo in repos:
#     print(repo['name'], repo['html_url'])

---------------------------------

Example using PyGithub:
---------------------------------
from github import Github

def fetch_repos_with_pygithub(token):
    g = Github(token)
    user = g.get_user()
    repos = user.get_repos()
    for repo in repos:
        print(repo.name, repo.html_url)

# Usage:
# token = 'your_personal_access_token'
# fetch_repos_with_pygithub(token)

---------------------------------

Note:
- You can use these functions to populate the Project model dynamically.
- For now, use Django admin or fixtures to add placeholder projects.
"""