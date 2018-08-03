echo "============================="
echo "     Runing the script       "
echo "============================="


python testToken

echo "============================="
echo "      Linting the code       "
echo "============================="

pylint -f parseable *.py | tee pylint.out
