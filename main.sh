
#------------------------Running the script---------------#

python3.6 testToken.py

#------------------------Linting the script---------------#

pylint -f parseable *.py | tee pylint.out

