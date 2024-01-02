pip install -r requirements.txt
pytest -s -v --html=Reports\report.html testCasesAdmin/ --browser chrome
pytest -s -v --html=Reports\report.html testCasesUser/ --browser chrome
pytest -s -v --html=Reports\report.html testNegativeAdmin/ --browser chrome
pytest -s -v --html=Reports\report.html testNegativeUser/ --browser chrome