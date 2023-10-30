from dropdown import dropdown_check
from checkbox import checkbox_check
from radiobutton import radio_button_check

from selenium import webdriver


def main():
    driver = webdriver.Chrome()

    # Launch the url in chrome
    driver.get("http://webdriveruniversity.com/index.html")
    driver.implicitly_wait(50)

    # Maximize the window
    driver.maximize_window()

    # Show page title
    print(driver.title)

    # call to dropdown function
    dropdown_check(driver)

    # call to checkbox
    checkbox_check(driver)

    # call to Radio Button
    radio_button_check(driver)

    # Close the current browser window
    driver.close()


if __name__ == "__main__":
    main()
