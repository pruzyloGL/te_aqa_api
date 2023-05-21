from src.config.config import Config
import requests


class GitHubAPIClient:

    # def __call__(self, *args: Any, **kwds: Any) -> Any:
    #     pass

    # def __new__(cls) -> Self:
    #     pass

    def __init__(self) -> None:
        pass

    def login(self, username, password):
        print(f"DO LOGIN for {username} and {password}")

    def logout(self):
        print("DO LOGOUT")

    def search_repo(self, repo_name, per_page=30):
        """
        Search repository by a repo_name param
        Return list of repos name of existing repos
        """
        # sendgin the request
        r = requests.get(
            url=f"{Config.get_property('API_BASE_URL')}/search/repositories",
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            # add query parameter
            params={
                'q': repo_name,
                'per_page': per_page
            },
        )
        print("Get Search Repo Response Status Code:", r.status_code)

        # throw an error if response is not 2xx and 3xx
        # optional
        r.raise_for_status()
        
        # get body
        body = r.json()

        body_repo_names = [x['name'] for x in body['items']]
        
        return body_repo_names
    
    def get_emojis(self):
        """
            Get list of available emojis in github sustem
        """

        r = requests.get(
            url=f"{Config.get_property('API_BASE_URL')}/emojis",
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            }
        )
        print("Get Emojis Response Status Code:", r.status_code)
        
        r.raise_for_status()
        body = r.json()
        list_of_emojis = body.keys()

        return list_of_emojis

    def search_topics(self, topics):
        """
        Search repository by topic name param
        Return list of existing topics
        """

        r = requests.get(
            url=f"{Config.get_property('API_BASE_URL')}/search/topics",
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            # add query parameter
            params={
                'q': topics,
            },
        )
        print("Get Search Topics Response Status Code:", r.status_code)

        # throw an error if response is not 2xx and 3xx
        # optional
        r.raise_for_status()

        # get body
        body = r.json()

        body_topics = [x['name'] for x in body['items']]

        return body_topics