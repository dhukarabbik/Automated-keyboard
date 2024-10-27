import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


# Setup WebDriver
options = Options()
options.add_argument("--start-maximized")
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"


service = Service(r"C:\key board script\geckodriver-v0.35.0-win32\geckodriver.exe")
driver = webdriver.Firefox(service=service, options=options)


# Open the Typist app login page
url = "https://typistapp.ca/#/welcome"
driver.get(url)
time.sleep(5)


# Fill in the login form
try:
    username_input = driver.find_element(By.ID, "usernameInput")
    password_input = driver.find_element(By.ID, "passwordInput")


    # Find the login button
    login_button = driver.find_element(By.XPATH, "//i[contains(@class, 'fa-long-arrow-right')]/ancestor::button")


    # Input credentials
    username_input.send_keys("")  # Replace with your username
    password_input.send_keys("")  # Replace with your password
    login_button.click()
except Exception as e:
    print(f"Error logging in: {e}")
    driver.quit()
    exit()


# Wait for the typing test area to load
time.sleep(5)


# Wait for the user to press Enter to start typing
input("Press Enter to start typing...")


# Now automate typing on the test
try:
    while True:
        # Continuously locate the elements containing the text to type
        text_elements = driver.find_elements(By.XPATH, "//span[@class='ng-binding letter' or @class='ng-binding space']")


        # Construct the text to type
        test_text = ''
        for element in text_elements:
            # Add spaces for space elements
            if 'space' in element.get_attribute("class"):
                test_text += ' '
            else:
                test_text += element.text


        # Wait for the typing input area to be ready
        typing_area = driver.find_element(By.TAG_NAME, "body")  # Use the body as the typing area


        # Simulate typing each character based on the displayed text
        for char in test_text:
            typing_area.send_keys(char)  # Type the character
            time.sleep(0.245)  # Maintain consistent timing for WPM


        # Wait for the new text to load if there are more lines to type
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='ng-binding letter' or @class='ng-binding space']")))


except Exception as e:
    print(f"Error during typing test: {e}")
finally:
    driver.quit()