"""Project2TestCases.py"""
# Import necessary libraries and modules for Selenium and project-specific functions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import TestLocators
from Data import WebData
from ExcelFunctions import ExcelFunctions

# Define the test case class that inherits from WebData and TestLocators.
class Project02TestCases(WebData, TestLocators):
    # Constructor for initializing the class
    def __init__(self):
        # Get the base URL from WebData
        self.url = WebData().url
        # Initialize Chrome driver.
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Set up an explicit wait.
        self.wait = WebDriverWait(self.driver, 10)
        # Maximize the browser window.
        self.driver.maximize_window()
        # Navigate to the specified URL.
        self.driver.get(self.url)
        # Initialize Excel functions
        self.xlobj = ExcelFunctions(WebData().excel_file, WebData().sheet_number)

    # Login method using credentials from Excel
    def login(self, username_row, password_row):
        # Read username and password from Excel
        username = self.xlobj.read_data(username_row, 9)
        password = self.xlobj.read_data(password_row, 10)
        try:
            # Wait for the username & password field and input data, then click login.
            self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().username_name))).send_keys(username)
            self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().password_name))).send_keys(password)
            self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().login_button))).click()
            print("Login successful.")
            # Return the current URL after login.
            return self.driver.current_url

        # Print error message if login fails.
        except Exception as error:
            print("Error during login:", error)
            return self.driver.current_url

    # Test case method for password reset functionality.
    def TC_PIM_01(self):
        try:
            # Read username for password reset from Excel.
            username = self.xlobj.read_data(2, 9)
            # Wait until the "Forgot Password" link is present and click it.
            self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().forget_password))).click()
            # Wait until the username and password field are present and enter the username and click reset button.
            self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().username_name))).send_keys(username)
            self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().reset_password_btn))).click()

            # Wait for the reset confirmation message to be present.
            reset_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().reset_message)))
            # Get the text of the reset message.
            reset_password_msg = reset_msg.text
            print(reset_password_msg)
            # Return the reset password message.
            return reset_password_msg

        # Print error if any occurs.
        except Exception as error:
            print("Error while resetting password:", error)

    # Test case method for validating admin headers.
    def TC_PIM_02(self):
        # Log in using specified rows from Excel.
        self.login(3, 3)
        try:
            # Wait until the admin link is present and locate it.
            admin = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, TestLocators().admin_text)))
            # Check if the admin element is visible
            if admin.is_displayed():
                # Click the admin link
                admin.click()
                # Get the current page title.
                page_title = self.driver.title
                print("TITLE:", page_title)
            # Return false if the admin link is not visible.
            else:
                print("Error: TITLE cannot be fetched")
                return False

            # Check header elements for their visibility and clickability
            elements_to_check = {"User Management": (By.XPATH, TestLocators().user_management),
                                 "Job": (By.XPATH, TestLocators().job),
                                 "Organisation": (By.XPATH, TestLocators().organization),
                                 "Qualification": (By.XPATH, TestLocators().qualifications),
                                 "Nationalities": (By.XPATH, TestLocators().nationalities),
                                 "Corporate Branding": (By.XPATH, TestLocators().corporate_branding),
                                 "Configuration": (By.XPATH, TestLocators().configuration)}

            # Loop through each element and check visibility and clickability.
            for name, element in elements_to_check.items():
                header_element = self.wait.until(EC.presence_of_element_located(element))

                # Check visibility and clickability
                if header_element.is_displayed():
                    print( name, " is visible.")
                    # Wait until the element is clickable.
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
                    header_element.click()
                    # Print clicked element name.
                    print("Clicked on ", name)
                    print("  ")

                # Return title and false if not visible.
                else:
                    print(name, " is not visible.")
                    return page_title, False
            # Print success message for validations.
            print("Fuctionality of all 7 Header elements are validated")
        # Print error if any occurs.
        except Exception as error:
            print("Error during navigation or element checks:", error)
            return page_title, False

        # Return title and success.
        return page_title, True  # Return title and success

    # Test case method for validating side menu functionalities.
    def TC_PIM_03(self):
        self.login(4, 4)
        try:
            # Wait until the admin link is present and locate it.
            admin = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, TestLocators().admin_text)))
            admin.click()

            # Define multiple menu options to check their visibility and clickability.
            menu_options = {"Admin": (By.XPATH, TestLocators().admin),
                                 "PIM": (By.XPATH, TestLocators().pim),
                                 "Leave": (By.XPATH, TestLocators().leave),
                                 "Time": (By.XPATH, TestLocators().time),
                                 "Recruitment": (By.XPATH, TestLocators().recruitment),
                                 "My Info": (By.XPATH, TestLocators().my_info),
                                 "Performance": (By.XPATH, TestLocators().performance),
                                 "Dashboard": (By.XPATH, TestLocators().dashboard),
                                 "Directory": (By.XPATH, TestLocators().directory),
                                 "Maintenance": (By.XPATH, TestLocators().maintenance),
                                 "Claim": (By.XPATH, TestLocators().claim),
                                 "Buzz": (By.XPATH, TestLocators().buzz)}

            # Loop through each menu option and check visibility and clickability.
            for name, element in menu_options.items():
                header_element = self.wait.until(EC.presence_of_element_located(element))

                # Check if the element is visible.
                if header_element.is_displayed():
                    print( name, " is visible.")
                    # Wait until the element is clickable.
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
                    # Click the element and print the validated element
                    header_element.click()
                    print("Clicked on ", name)
                    # Empty string as line breaks for readability in output
                    print("  ")
                    # Handle the popup on the Maintenance page
                    if name == "Maintenance":
                        try:
                            # Wait for the cancel button on the popup to be visible and clickable
                            cancel_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH,TestLocators.cancel_button)))
                            cancel_btn.click()
                        # Print error if cancel button handling fails
                        except Exception as e:
                            print("Cancel button not found or clickable:", e)
                # Print visibility error and return false
                else:
                    print(name, " is not visible.")
                    return False
                    # Print success message for validations.
            print("Fuctionality of all 12 Side pane menu elements are validated")

        # Print error if any occurs.
        except Exception as error:
            print("Error during navigation or element checks:", error)
            return False

        # Return success
        return True

    # Method to close the browser driver.
    def close_driver(self):
        # Quit the browser and close the driver.
        self.driver.quit()