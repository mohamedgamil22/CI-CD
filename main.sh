
#------------------------Running the script---------------#

python3.6 testToken.py
#test
#------------------------Linting the script---------------#

pylint -f parseable *.py | tee pylint.out

