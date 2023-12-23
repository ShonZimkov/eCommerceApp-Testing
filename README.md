In this project I created a framework from scratch that makes Automation Testing Easier for Testing an eCommerce App.
The Objective was to ensure Re-usability and Maintainability while Organizly Making new Test cases.
In the project i used tools, techniques and technologies such as:
Python, Selenium WebDriver, Pytest, POM (Page Object Model), HTML Reports.

To run simply use the following commands:
pip install -r requirements.txt

To run all sanity tests:
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
