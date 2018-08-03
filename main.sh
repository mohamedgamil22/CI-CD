
#------------------------Running the script---------------#

python testToken.py

#------------------------Linting the script---------------#

pylint -f parseable *.py | tee pylint.out

