Role: Solely automated testing of an e-commerce platform for comprehensive quality assurance.
Programming Language: Utilized Python for test script development.
Testing Framework: Implemented tests using the PyTest framework for efficient and scalable automation.
Design Pattern: Employed the Page Object Model (POM) design pattern for a modular and maintainable testing framework.
Web Automation: Utilized Selenium WebDriver for web application automation, ensuring reliable and consistent test execution.
Reporting: Integrated HTML reports to provide detailed and actionable insights into test results.
Agile Methodology: Utilized Jira for Agile Scrum methodology management in personal project management.
Test Management: Employed Zephyr Scale as a test management tool for organized test planning, execution, and reporting.
Continuous Integration/Continuous Deployment (CI/CD): Designed and executed tests seamlessly within Jenkins for efficient CI/CD pipelines.

To run simply use the following commands:
pip install -r requirements.txt

To run all sanity tests:
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome

To run all Customer POV tests:
pytest -s -v --html=./Reports/report.html testCasesUserP/ --browser chrome

To run all Admin POV tests:
pytest -s -v --html=./Reports/report.html testCases/ --browser chrome

*To run in different browser simply write instead of chrome, firefox and to run on MS edge, leave blank
