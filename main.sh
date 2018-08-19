
#------------------------Running the script---------------#

python3.6 fe_iam.py
#test
#------------------------Linting the script---------------#

pylint -f parseable *.py | tee pylint.out

