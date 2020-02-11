
# Become familiar with testing terms:
#             We use ISTQB terminology. A good place to start is the Foundation Level:
#                         https://www.istqb.org/certification-path-root/foundation-level-2018.html
#                         Learn testing terms:
#                                     Boundary Testing
#                                     Smoke Testing
#                                     Regression Testing
#                                     Unit vs Integration Testing
# Python
#             You have already installed and started doing “Hello World” applications in python. Try following:
#                         Go to facebook.com
#                         Find the Button/Element “Sign Up”
#                         Bonus – Put a name into the First name field.

import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver_to_use = "/Users/bjackson/Repo/webdriver/chromedriver"

def test_face_book_sign_up():

    driver = webdriver.Chrome(
                executable_path=driver_to_use)
    driver.get("http://www.facebook.com")
    time.sleep(1)
    test = check_exists_by_css_path(driver,'button#u_0_13')
    print(test)
    assert test is True
    driver.close()

def test_name_in_first_name_field():
    driver = webdriver.Chrome(
        executable_path=driver_to_use)
    first_name = "helloOrie"
    driver.get("http://www.facebook.com")
    time.sleep(3)
    driver.find_element_by_css_selector('input#u_0_m').send_keys(first_name)
    time.sleep(3)
    assert driver.find_element_by_css_selector('input#u_0_m').get_attribute("value") == first_name
    driver.close()


def check_exists_by_css_path(driver ,css_path):
    try:
        driver.find_element_by_css_selector(css_path)
    except NoSuchElementException:
        return False
    return True