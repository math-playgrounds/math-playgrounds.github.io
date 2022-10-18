APP=mathplayground

include *.mk

jenkins: check flake8 test
