"""common.py"""

# Import classes from their modules
from Project2TestCases import Project02TestCases
from Data import WebData
from ExcelFunctions import ExcelFunctions

# Initialize common resources
excel_file = WebData().excel_file
sheet_number = WebData().sheet_number
# Creates an instance of ExcelFunctions which handles Excel operations.
xlobj = ExcelFunctions(excel_file, sheet_number)

# Defines a function that returns an instance of the Project02TestCases class.
def get_test_case_instance():
    return Project02TestCases()
