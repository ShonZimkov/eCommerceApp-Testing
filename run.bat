virtualenv venv --distribute
. venv/bin/activate
pip install -r requirements.txt
pytest -s -v -m sanity --html=Reports\report.html testCases/ --browser chrome
