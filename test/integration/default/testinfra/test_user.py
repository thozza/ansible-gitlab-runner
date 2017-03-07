

def test_gitlab_user_exists(User):
    user = User('gitlab-runner')
    assert user.exists
