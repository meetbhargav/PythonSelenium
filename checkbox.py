
def checkbox_check(driver):

    checked_option = driver.find_element(by='xpath', value='//input[@value="option-1"]')
    checked_option.click()

    checkboxes = driver.find_elements(by='xpath', value="//input[@type='checkbox']")

    checked_count = 0
    unchecked_count = 0

    for checkbox in checkboxes:
        if checkbox.is_selected() :
            checked_count = checked_count + 1
        else:
            unchecked_count = unchecked_count + 1

    print(f"Checked count: {checked_count}")
    print(f"Unchecked count: {unchecked_count}")

