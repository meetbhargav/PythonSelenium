import pytest

from test_dropdown import test_dropdown_check
from test_checkbox import test_checkbox_check
from test_radiobutton import test_radio_button_check

from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Chrome()

    # Launch the url in chrome
    driver.get("http://webdriveruniversity.com/index.html")
    driver.implicitly_wait(50)

    # Maximize the window
    driver.maximize_window()

    # Show page title
    print(driver.title)

    # Click on the DROPDOWN, CHECKBOXE(S) & RADIO BUTTON(S) link
    driver.find_element(by='xpath', value='//a[@id="dropdown-checkboxes-radiobuttons"]//h1').click()

    # Get window Handles to switch the control between them
    window_handles = driver.window_handles

    # Switch to new window - Index 1 is for new window
    driver.switch_to.window(window_handles[1])

    yield driver

    # Close the current browser window
    driver.close()
