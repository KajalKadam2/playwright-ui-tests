#
# test_checkboxes_pom.py
from pages.checkboxes_page import CheckboxesPage


def test_first_checkbox_starts_unchecked(checkboxes_page_obj: CheckboxesPage):
    checkboxes_page_obj.expect_unchecked(0)


def test_check_first_checkbox(checkboxes_page_obj: CheckboxesPage):
    (checkboxes_page_obj
        .check(0)
        .expect_checked(0))


def test_second_checkbox_starts_checked(checkboxes_page_obj: CheckboxesPage):
    checkboxes_page_obj.expect_checked(1)