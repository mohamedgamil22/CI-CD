echo "============================="
echo "     Runing the script       "
echo "============================="


python testToken.py

if [ ! $? -eq  0 ]
then

echo "============================="
echo "        script failed        "
echo "============================="

exit $?
fi

echo "============================="
echo "      Linting the code       "
echo "============================="

pylint -f parseable *.py | tee pylint.out

