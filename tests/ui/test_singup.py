import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


#driver = webdriver.Chrome()
user_name = "user"
user_pass = "user"
browser = "chrome"


@pytest.fixture()
def selenium_fixture():
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_signup_negative(selenium_fixture):
    driver = selenium_fixture
    driver.get("https://github.com/login")

    login_field = driver.find_element(By.ID, "login_field")
    login_field.send_keys(user_name)
    pass_field = driver.find_element(By.ID, "password")
    pass_field.send_keys(user_pass)
    login_btn = driver.find_element(By.NAME, "commit")
    login_btn.click()
    login_alert = driver.find_element(By.CLASS_NAME, "js-flash-alert")

    assert login_alert.text.__contains__("Incorrect username or password")


def test_signup_positive(selenium_fixture):
    driver = selenium_fixture
    driver.get("https://github.com/login")

    login_field = driver.find_element(By.ID, "login_field")
    login_field.send_keys(user_name)
    pass_field = driver.find_element(By.ID, "password")
    pass_field.send_keys(user_pass)
    login_btn = driver.find_element(By.NAME, "commit")
    login_btn.click()

    assert driver.current_url == "https://github.com/"
