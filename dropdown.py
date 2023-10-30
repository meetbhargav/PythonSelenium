import time
from selenium.webdriver.support.select import Select


def dropdown_check(driver):
    # Click on the DROPDOWN, CHECKBOXE(S) & RADIO BUTTON(S) link
    driver.find_element(by='xpath', value='//a[@id="dropdown-checkboxes-radiobuttons"]//h1').click()

    # Get window Handles to switch the control between them
    window_handles = driver.window_handles

    # Switch to new window - Index 1 is for new window
    driver.switch_to.window(window_handles[1])

    # Select Values from Dropdown
    dropdown = Select(driver.find_element(by='xpath', value='//select[@id="dropdowm-menu-1"]'))
    dropdown.select_by_value('python')

    # Comparison -
    if dropdown.first_selected_option.get_attribute('value') == "python":
        print("Selected value is Python")
    else:
        print("Selected value is other than the value expected")

    # for 3 seconds delay to see the execution
    time.sleep(3)
