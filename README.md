![Test Status](https://github.com/adheenacv/ReactJSTestProjectPython/actions/workflows/main.yml/badge.svg?branch=main)

# A pytest project using selenium to automate the ReactJS components

A basic POM implementation using Selenium, Python and pytest to automate functionalities of ReactJS based components.

## Environment Setup:

1. Install Python version 3.11
2. Install PyCharm IDE

## Working with this repository:

1. Clone the repo: `git clone git@github.com:adheenacv/ReactJSTestProjectPython.git`
2. Install dependencies by running the command at the root folder of the project - `pip install -r requirements.txt`

## Knowing the project folder structure:

* ./components/ - ReactJS based components are designed here. 
* ./pages/ - ReactJS pages are designed here. 
* ./tests/ - TDD based tests are captured here. 
* ./util/ - General utilities are captured here. 

## Executing the tests in your local machine:

* Execute a single module from IDE - Right click on the file (module to be executed) from Project Explorer 
* Execute a single module from console - Execute the command `pytest <path_to_the_module>` 
* Execute entire suite - Execute the command `pytest ./tests/` from the root folder of the project 
