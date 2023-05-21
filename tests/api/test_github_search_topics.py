def test_search_topics_positive(fixture_git_hub_api_client):
    """
    test for existing topics
    """
    topics = "ruby"
    topics_list = fixture_git_hub_api_client.search_topics(topics)
    print(f'asserting {topics} in searched topics')
    assert topics in topics_list

def test_search_topics_negative(fixture_git_hub_api_client):
    """
    negative test for existing topics
    """
    topics = "asdasd222282"
    topics_list = fixture_git_hub_api_client.search_topics(topics)
    print(f'asserting {topics} not in searched topics')
    assert topics not in topics_list

def test_search_topics_count(fixture_git_hub_api_client):
    """
    negative test for existing topics
    """
    topics = "ruby"
    topics_count = fixture_git_hub_api_client.search_topics_count(topics)
    print(f'the count of topics is {topics_count} ')
    assert topics_count > 0






