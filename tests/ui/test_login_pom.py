#

# test_login_pom.py
import pytest
from pages.login_page import LoginPage


def test_valid_login(login_page_obj: LoginPage):
    (login_page_obj
        .login("tomsmith", "SuperSecretPassword!")
        .expect_success())


def test_invalid_username(login_page_obj: LoginPage):
    (login_page_obj
        .login("wronguser", "wrongpass")
        .expect_error("Your username is invalid")
        .expect_url_is_login())


def test_invalid_password(login_page_obj: LoginPage):
    (login_page_obj
        .login("tomsmith", "wrongpass")
        .expect_error("Your password is invalid"))


def test_empty_fields(login_page_obj: LoginPage):
    (login_page_obj
        .login("", "")
        .expect_error("Your username is invalid"))


@pytest.mark.parametrize("username, password, error", [
    ("wronguser", "pass",  "Your username is invalid"),
    ("tomsmith",  "wrong", "Your password is invalid"),
    ("",          "",      "Your username is invalid"),
], ids=["wrong_user", "wrong_pass", "empty"])
def test_invalid_logins_parametrized(login_page_obj: LoginPage,
                                     username, password, error):
    (login_page_obj
        .login(username, password)
        .expect_error(error))