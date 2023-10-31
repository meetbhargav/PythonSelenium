import time
from selenium.webdriver.support.select import Select


def test_dropdown_check(setup):
    driver = setup

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
