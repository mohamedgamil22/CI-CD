echo "============================="
echo "     Runing the script       "
echo "============================="


python testToken.py
retCode=$?

if [ ! $retCode -eq  0 ]
then

echo "============================="
echo "        script failed        "
echo "============================="

echo "python return code is" $retCode
exit 1
fi

echo "============================="
echo "      Linting the code       "
echo "============================="

pylint -f parseable *.py | tee pylint.out

