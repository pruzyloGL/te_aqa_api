import requests
import pytest

def test_emoji_could_be_retrived():
    r = requests.get(
        # url
        url="https://api.github.com/emojis",
        # query params
        params={
            'q': "sergii"
        },
        # headers
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        # body option#1
        json={},
        # body option#2
        data = {}
        )
    
    r.raise_for_status()

    print("Response Status Code:", r.status_code)
    print("Response Cache Header:", r.headers['Cache-Control'])

    assert 'v8' in r.json()['zzz'] 


@pytest.fixture(scope='module')
def list_of_emojis(fixture_git_hub_api_client):
    yield fixture_git_hub_api_client.get_emojis()

def test_emoji_could_be_retrived_2(list_of_emojis):
    assert len(list_of_emojis) != 0
    
def test_emoji_zzz_exists(list_of_emojis):
    assert 'zzz' in list_of_emojis

def test_emoji_sergii_doesnt_exist(list_of_emojis):    
    assert 'sergii' not in list_of_emojis
