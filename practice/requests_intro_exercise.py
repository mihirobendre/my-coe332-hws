
import requests

def get_github_org_info(org_id):
    base_url = f"https://api.github.com/orgs/{org_id}"
    headers = {
        "Accept": "application/vnd.github.v3+json"  # Specify version of GitHub API
    }

    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        org_info = response.json()
        return org_info
    else:
        print(f"Failed to retrieve information for organization {org_id}. Status code: {response.status_code}")
        return None

def get_github_org_members(org_id):
    base_url = f"https://api.github.com/orgs/{org_id}/members"
    headers = {
        "Accept": "application/vnd.github.v3+json"  # Specify version of GitHub API
    }

    members = []

    # GitHub API paginates results, so we need to handle multiple pages if necessary
    while base_url:
        response = requests.get(base_url, headers=headers)

        if response.status_code == 200:
            members_info = response.json()
            for member in members_info:
                members.append(member['login'])
            # Check if there are more pages
            base_url = response.links.get('next', {}).get('url')  
        else:
            print(f"Failed to retrieve members for organization {org_id}. Status code: {response.status_code}")
            return None

    return members

def get_github_org_repositories(org_id):
    base_url = f"https://api.github.com/orgs/{org_id}/repos"
    headers = {
        "Accept": "application/vnd.github.v3+json"  # Specify version of GitHub API
    }

    repositories = []

    # GitHub API paginates results, so we need to handle multiple pages if necessary
    while base_url:
        response = requests.get(base_url, headers=headers)

        if response.status_code == 200:
            repos_info = response.json()
            for repo in repos_info:
                repositories.append(repo['full_name'])
            # Check if there are more pages
            base_url = response.links.get('next', {}).get('url')  
        else:
            print(f"Failed to retrieve repositories for organization {org_id}. Status code: {response.status_code}")
            return None

    return repositories


# testing get_github_org_info:
org_id = "github"  # Replace with the desired GitHub organization ID
org_info = get_github_org_info(org_id)
if org_info:
    print(org_info)

# testing get_github_org_members:
org_id = "github"  # Replace with the desired GitHub organization ID
org_members = get_github_org_members(org_id)
if org_members:
    print(org_members)

# testing get_github_org_repositories:
org_id = "github"  # Replace with the desired GitHub organization ID
org_repositories = get_github_org_repositories(org_id)
if org_repositories:
    print(org_repositories)


