# Python --
# On facebook.com fill out all data fields, and create assert statements to verify data in the field matches what was entered.
# This can be done in one test or as many tests as you would like to complete the task.
# QA --
# Create 10 test case titles for testing the email field.
#


import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver_b1 = "/Users/bjackson/Repo/webdriver/chromedriver"


@pytest.fixture(params=["chrome"], scope='module')
def driver_init(request):
    web_driver = webdriver.Chrome(executable_path=driver_b1)

    def close_browser():
        try:
            web_driver.close()
        except NoSuchElementException:
            print("tests did not setup correctly. Closing page.")
            web_driver.close()

    request.addfinalizer(close_browser)
    return web_driver


@pytest.fixture(scope='module')
def driver_login(driver_init):
    driver_init.maximize_window()
    driver_init.get("http://www.facebook.com")
    return driver_init


def test_fill_out_sign_up_page(driver_init, driver_login):
    time.sleep(1)
    driver_init.find_element_by_css_selector('input#u_0_m').send_keys("Arrow")
    driver_init.find_element_by_css_selector('input#u_0_o').send_keys("Bee")
    driver_init.find_element_by_css_selector('input#u_0_r').send_keys("801-555-5555")
    driver_init.find_element_by_css_selector('input#u_0_w').send_keys("801BreakIt!")
    driver_init.find_element_by_xpath("//select[@id='month']").send_keys("Jun")
    driver_init.find_element_by_xpath("//select[@id='day']").send_keys("24")
    driver_init.find_element_by_xpath("//select[@id='year']").send_keys("1980")
    driver_init.find_element_by_css_selector('input#u_0_9').click()
    time.sleep(1)
    assert driver_init.find_element_by_css_selector('input#u_0_m').get_attribute("value") == "Python"
    assert driver_init.find_element_by_css_selector('input#u_0_o').get_attribute("value") == "801"
    assert driver_init.find_element_by_css_selector('input#u_0_r').get_attribute("value") == "801-555-5555"
    assert driver_init.find_element_by_css_selector('input#u_0_w').get_attribute("value") == "801BreakIt!"
    assert driver_init.find_element_by_xpath("//select[@id='month']").get_attribute("value") == "6"
    assert driver_init.find_element_by_xpath("//select[@id='day']").get_attribute("value") == "24"
    assert driver_init.find_element_by_xpath("//select[@id='year']").get_attribute("value") == "1980"
    assert driver_login.find_element_by_css_selector("input#u_0_9:checked[type='radio']")


