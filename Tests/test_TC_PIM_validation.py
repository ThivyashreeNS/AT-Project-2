"""test_TC_PIM_validation.py"""

# Import pytest for test case management and TestLocators for element locators.
import pytest
from Locators import TestLocators
# Import shared resources
from common import get_test_case_instance, xlobj

# Define the test case for checking the admin page title and header elements visibility
def test_TC_PIM_02():
    shree = get_test_case_instance()
    # Get the expected title from TestLocators.
    test_title = TestLocators.title
    # Call the TC_PIM_02 method and get the actual title and status
    fetched_title, elements_status = shree.TC_PIM_02()
    # Check title and write to excel file
    assert fetched_title == test_title
    print("Title of the Webpage is", test_title)
    xlobj.write_data(3, 12, test_title)

    # Assert that all elements are visible and clickable.
    assert elements_status, "One or more element checks failed."
    print("Headers on the Admin Page are Visible, displayed and Clickable")
    # Read existing content from the cell
    existing_data = xlobj.read_data(3, 12)
    # Append new data to the existing data
    new_data = f"{existing_data}\n{elements_status}"  # Use \n for a line break
    # Write the combined data back to the cell
    xlobj.write_data(3, 12, new_data)
    shree.close_driver()

# Define the test case for checking the side pane functionality.
def test_TC_PIM_03():
    shree = get_test_case_instance()
    # Call the TC_PIM_03 method to check menu status.
    menu_status = shree.TC_PIM_03()
    # Assert that all menu items are visible and clickable.
    assert menu_status, "One or more element checks failed."
    # Write menu status to Excel
    xlobj.write_data(4, 12, menu_status)
    # Close the browser driver.
    shree.close_driver()
    