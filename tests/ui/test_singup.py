import time

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.user import User

driver = webdriver.Chrome()
user_name = "user"
user_pass = "user"

@pytest.fixture
def specific_sign_up_user_fixture():
    yield 42


def test_signup_negative():
    driver.get("https://github.com/login")

    login_field = driver.find_element(By.ID, "login_field")
    login_field.send_keys(user_name)
    pass_field = driver.find_element(By.ID, "password")
    pass_field.send_keys(user_pass)
    login_btn = driver.find_element(By.NAME, "commit")
    login_btn.click()
    login_alert = driver.find_element(By.CLASS_NAME, "js-flash-alert")

    assert login_alert.text.__contains__("Incorrect username or password")


def test_signup_positive():
    driver.get("https://github.com/login")

    login_field = driver.find_element(By.ID, "login_field")
    login_field.send_keys(user_name)
    pass_field = driver.find_element(By.ID, "password")
    pass_field.send_keys(user_pass)
    login_btn = driver.find_element(By.NAME, "commit")
    login_btn.click()

    assert driver.current_url == "https://github.com/"


def test_signup_final_negative(user_fixture):
    assert user_fixture.get('name') == 'aaaaaautomation_test_removein_30_days_non_existing_user'


def test_signup_final_positive(user_fixture):
    assert user_fixture.get('name') == User.username
