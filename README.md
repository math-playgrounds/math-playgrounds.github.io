# mathplayground_django
Django Channels server for mathplayground

## Start-up steps:
Install [https://redis.io/ Redis] and start the redis service.

Start django server:
```
python3 -m venv ve
./ve/bin/pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```
