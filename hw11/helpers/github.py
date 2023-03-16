import requests
import json

def get_github_repositories(query, page):
    response = requests.get("https://api.github.com/search/repositories?q=" + query + "&page=" + page)
    return response.content


def json_parser(body):
    data = json.loads(body)
    repositories = []
    for el in data["items"]:
        new_repo = {
            "name": el["name"],
            "full_name": el["full_name"],
            "private": el["private"],
            "description": el["description"]
        }
        repositories.append(new_repo)
    return repositories