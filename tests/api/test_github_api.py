import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exist(github_api):
    r = github_api.get_user("klekovkinaolena")
    assert r["message"] == "Not Found"
