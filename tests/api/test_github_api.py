import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api  # test user exist
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api  # test user not exist
def test_user_not_exist(github_api):
    r = github_api.get_user("klekovkinaolena")
    assert r["message"] == "Not Found"


@pytest.mark.api  # test repository can be found
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 31
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api  # test repository cannot be found
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("klekovkina_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api  # test searching repository with single char
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("o")
    assert r["total_count"] != 0


@pytest.mark.api  # test repository exist
def test_get_exist_repo(github_api):
    r = github_api.get_repo("klekovkina", "klekovkina_qa_auto")
    assert r["full_name"] == "klekovkina/klekovkina_QA_Auto"


@pytest.mark.api  # test repository not exist
def test_get_nonexist_repo(github_api):
    r = github_api.get_repo("klekovkina", "repo_non_exist")
    assert r["message"] == "Not Found"


@pytest.mark.api  # test repository exist, but private
def test_get_private_repo(github_api):
    r = github_api.get_repo("klekovkina", "klekovkina_qa_2023")
    assert r["message"] == "Not Found"
