# AT-Project-2

## Overview:
This project is designed for automating the testing of the OrangeHRM web application using Python, Selenium WebDriver, and Pytest. The focus is on verifying user login functionality, password reset operations, and validating various functionalities in the admin section.

## Table of Contents:
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Test Cases](#test-cases)
- [Running the Tests](#running-the-tests)
- [Test Data Configuration](#test-data-configuration)

- ## Features
- **User Authentication Testing**: Tests the login functionality with valid credentials and checks for error handling with invalid ones.
- **Password Reset Functionality**: Validates the process for resetting passwords.
- **Admin Page Headers Validation**: Checks for the visibility and clickability of various admin page elements.
- **Side Pane Menu Functionality**: Ensures that all side menu items are functional and accessible.
- **Excel Integration**: Reads from and writes test data to an Excel file for easy management and reporting.
- **Reusable Components**: Common functions and data are abstracted into separate modules for better maintainability.
- **Dynamic Waits**: Uses explicit waits for web elements to ensure stability during testing.
- **Data-Driven Testing Framework**: Utilizes Excel files for input data, allowing for flexible test execution with varying user credentials and admin functionalities.
- **Automation Framework**: Built using Selenium for browser automation and Pytest for test case management.

## Prerequisites
- Python 3.x
- Required libraries:
  - `selenium`
  - `pytest`
  - `openpyxl`
  - `webdriver-manager`

## Installation
To successfully set up and run the Selenium Automation Testing Project, follow these steps:

1. Ensure that you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/).

2. Familiarity with command-line interface (CLI) tools is recommended for executing commands.

3. Set Up a Virtual Environment (Optional but Recommended):
   - It's best practice to create a virtual environment to manage dependencies for your project:
     
     - Verify Python Virtual Environment: `Virtualenv --version`
       
     - Create Virtual Environment:  `virtualenv cd`
       
     - Activate Virtual Environment:  `Scripts\Activate`
       
     - Deactivate Virtual Environment: `Scripts\Deactivate`
       
4.  Install Required Libraries:
    - Install the necessary Python libraries using pip. The required libraries for this project include:
      - __Selenium :__ For web browser automation.
        Install Python Selenium Module: `pip install selenium`
        
      - __Pytest :__ For running test cases and managing test execution.
        `pip install pytest`
         Pytest Report: `pip install pytest-html`
        
      - __openpyxl :__ For reading and writing Excel files.
         `pip install selenium openpyxl`
        
      - __Webdriver-manager :__ To automatically manage browser drivers.
          Install WebDriver Manager Module: `pip install webdriver-manager`

## Project Structure:
```python
AT_Project_2 
├── Data.py                          # Contains the WebData class for test data and configuration.
│   └── class WebData:
├── Locators.py                      # Defines the TestLocators class for web element locators.
│   └── class TestLocators:
├── ExcelFunctions.py                # Contains the ExcelFunctions class for reading and writing Excel files.
│   └── class ExcelFunctions:
├── Project2TestCases.py             # Contains the Project2TestCases class with test case implementations (main file).
│   ├── def login():                 # Login method
│   ├── def TC_PIM_01():             # Test case for Reset password
│   ├── def TC_PIM_02():             # Test case for Validate header 
│   └── def TC_PIM_03():             # Test case for Validate side menu 
├── Tests/
│   ├── test_TC_PIM_01.py            # Test case for password reset.
│   │   └── def test_TC_PIM_01():
│   └── test_TC_PIM.py               # Test cases for admin page and side menu functionality.
│       ├── def test_TC_PIM_02():    # Test case for admin page header validation.
│       └── def test_TC_PIM_03():    # Test case for side menu functionality.
├── common.py                        # Initializes common resources for tests.
└── project2_data.xlsx               # Excel file containing test data.
└── Reports/
    ├── passwordReset.html           # Pytest HTML Report for the password reset test suite.
    └── adminValidationReport.html   # Pytest HTML Report for the admin validation tests.
```

## Test Cases:
### Password Reset Tests
- **test_TC_PIM_01**: Tests the password reset functionality using credentials from Excel.

### Admin Page Tests
- **test_TC_PIM_02**: Validates the title and checks visibility of admin page elements.

### Side Menu Tests
- **test_TC_PIM_03**: Validates functionality of all side menu items.

## Running the Tests:
- __To run all test cases:__
  - To execute all test cases in the project, navigate to the project directory and use the following command:	`pytest`
  -This command will automatically discover and run all test files that match the pattern **test_*.py**

- __Running Specific Tests:__
  - To run a specific test case, specify the test file and the test function. For example, to run the PIM test cases, use:
                  `pytest test_PIM_validation.py`
  - To run a specific test within that file, use: `pytest test_PIM_validation.py::test_TC_PIM_02`
  
- __Generate a Report:__
  -  To create an HTML report of the test results, you can use:
     ```
     pytest -v -s --capture=sys --html=Reports\adminValidationReport.html test_PIM_validation.py
     ```
     
- __Viewing Test Results:__
  - After running the tests, results will be displayed in the terminal. You will see the status of each test (passed, failed, etc.), along with any relevant output or error messages.
    
  - Check the output in the console for test results. Successful tests will also update the corresponding results in *project2_data.xlsx*.
    
  - The pytest html report will be generated and saved in the Reports folder.
 
## Test Data Configuration:
- Ensure that the *project2_data.xlsx* file is properly configured with the necessary test credentials and data for your tests to execute correctly.
  
- Check the output in the console for test results. Successful tests will also update the corresponding results in *project2_data.xlsx*.





