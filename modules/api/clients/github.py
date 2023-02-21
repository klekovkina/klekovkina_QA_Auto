import requests


class GitHub:
    # get user
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    # search repository
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body

    # get repository
    def get_repo(self, own, repo):
        r = requests.get(f"https://api.github.com/repos/{own}/{repo}")
        body = r.json()

        return body
