# Use pytest to create the following two tests.
# The tests should only create one chrome webdriver  (use pytest fixtures for this) to execute both tests.
#             First test:
#                           Find the Button/Element “Sign Up” on facebook.com
#             Second test:
#                         Put a name into the First name field.
#             Bonus:
#                         Fill out all data fields for creating an account
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


def test_face_book_first_test(driver_init, driver_login):
    time.sleep(1)
    test = check_exists_by_css_path(driver_init, 'button#u_0_13')
    print(test)
    assert test is True


def test_name_in_first_name_field_second_test(driver_init, driver_login):
    first_name = "helloOrie"
    time.sleep(3)
    driver_init.find_element_by_css_selector('input#u_0_m').send_keys(first_name)
    time.sleep(3)
    assert driver_init.find_element_by_css_selector('input#u_0_m').get_attribute("value") == first_name


####################BONUS####################

def test_fill_out_sign_up_page(driver_init, driver_login):
    time.sleep(1)
    driver_init.find_element_by_css_selector('input#u_0_m').send_keys("Python")
    driver_init.find_element_by_css_selector('input#u_0_o').send_keys("801")
    driver_init.find_element_by_css_selector('input#u_0_r').send_keys("801-555-5555")
    driver_init.find_element_by_css_selector('input#u_0_w').send_keys("801BreakIt!")
    driver_init.find_element_by_xpath("//select[@id='month']").send_keys("Jun")
    driver_init.find_element_by_xpath("//select[@id='day']").send_keys("24")
    driver_init.find_element_by_xpath("//select[@id='year']").send_keys("1980")
    driver_init.find_element_by_css_selector('input#u_0_9').click()
    time.sleep(1)
    assert driver_init.find_element_by_css_selector('input#u_0_m').get_attribute("value") == "Python"




def check_exists_by_css_path(driver, css_path):
    try:
        driver.find_element_by_css_selector(css_path)
    except NoSuchElementException:
        return False
    return True
