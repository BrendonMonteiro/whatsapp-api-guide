import os
import requests
import re
import json

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = "Avielzi"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_public_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos?type=public"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_repo_stats(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    data = response.json()
    
    # Traffic views require push access, if fails we skip
    views = 0
    try:
        traffic_url = f"https://api.github.com/repos/{owner}/{repo}/traffic/views"
        traffic_res = requests.get(traffic_url, headers=HEADERS)
        if traffic_res.status_code == 200:
            views = traffic_res.json().get("count", 0)
    except:
        pass
        
    return {
        "stars": data.get("stargazers_count", 0),
        "forks": data.get("forks_count", 0),
        "watchers": data.get("subscribers_count", 0),
        "views": views
    }

def update_readme_stats(owner, repo, stats):
    readme_url = f"https://api.github.com/repos/{owner}/{repo}/contents/README.md"
    response = requests.get(readme_url, headers=HEADERS)
    if response.status_code != 200:
        print(f"No README found for {repo}")
        return

    content_data = response.json()
    import base64
    content = base64.b64decode(content_data["content"]).decode("utf-8")

    stats_section = f"""
<!-- REPO_STATS_START -->
### 📊 Repository Status
| Stars | Forks | Watchers | Views |
| :---: | :---: | :---: | :---: |
| {stats['stars']} | {stats['forks']} | {stats['watchers']} | {stats['views']} |
<!-- REPO_STATS_END -->
"""
    
    pattern = r"<!-- REPO_STATS_START -->.*?<!-- REPO_STATS_END -->"
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, stats_section.strip(), content, flags=re.DOTALL)
    else:
        new_content = content + "\n" + stats_section

    if new_content != content:
        update_data = {
            "message": "docs: update repository statistics [skip ci]",
            "content": base64.b64encode(new_content.encode("utf-8")).decode("utf-8"),
            "sha": content_data["sha"]
        }
        requests.put(readme_url, headers=HEADERS, data=json.dumps(update_data))
        print(f"Updated stats for {repo}")

def auto_tag_repo(owner, repo, current_topics):
    # Core English tags for AI and Automation
    ai_tags = {"ai", "artificial-intelligence", "automation", "python", "api-safety"}
    new_topics = set(current_topics)
    
    # Check for keywords in repo name or topics to add AI tags
    keywords = ["ai", "bot", "gpt", "whatsapp", "automation", "api"]
    if any(kw in repo.lower() for kw in keywords):
        new_topics.update(ai_tags)
    
    if "whatsapp" in repo.lower():
        new_topics.add("whatsapp-api")
        new_topics.add("meta-api")

    if set(current_topics) != new_topics:
        url = f"https://api.github.com/repos/{owner}/{repo}/topics"
        data = {"names": list(new_topics)}
        requests.put(url, headers=HEADERS, data=json.dumps(data))
        print(f"Updated topics for {repo}: {list(new_topics)}")

def main():
    repos = get_public_repos()
    for repo in repos:
        name = repo["name"]
        owner = repo["owner"]["login"]
        topics = repo.get("topics", [])
        
        print(f"Processing {name}...")
        
        # 1. Update Topics (Auto-Tagging with English AI terms)
        auto_tag_repo(owner, name, topics)
        
        # 2. Sync Stats
        stats = get_repo_stats(owner, name)
        update_readme_stats(owner, name, stats)

if __name__ == "__main__":
    main()
