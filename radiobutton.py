import time


def radio_button_check(driver):
    radio_button = driver.find_element(by='xpath', value='//input[@value="green"]')
    radio_button.click()

    radio_options = driver.find_elements(by='xpath', value="//form[@id='radio-buttons']//input[@type='radio']")

    checked_radio_count = 0
    unchecked_radio_count = 0

    for radio in radio_options:
        if radio.is_selected():
            checked_radio_count += 1
        else:
            unchecked_radio_count += 1

    print(f'checked radio buttons: {checked_radio_count}')
    print(f'Unchecked radio buttons: {unchecked_radio_count}')

    time.sleep(5)
