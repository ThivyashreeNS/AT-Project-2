"""test_TC_PIM_01.py"""

# Import pytest for test case management and TestLocators for element locators.
import pytest
from Locators import TestLocators
# Import shared resources
from common import get_test_case_instance, xlobj

# Define the test case for resetting the password.
def test_TC_PIM_01():
    # Get an instance of the test case class.
    shree = get_test_case_instance()
    # Expected success message.
    test_msg = "Reset Password link sent successfully"
    # Assert that the returned message matches the expected and  write to Excel
    assert shree.TC_PIM_01() == test_msg
    xlobj.write_data(2, 12, test_msg)
    # Close the browser driver.
    shree.close_driver()




