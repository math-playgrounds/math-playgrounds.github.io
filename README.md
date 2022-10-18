# mathplayground_django
Django Channels server for mathplayground. Structure based on: https://channels.readthedocs.io/en/latest/tutorial/index.html


## Start-up steps:
Install [Redis](https://redis.io/) and start the redis service.

Start django server:
```
python3 -m venv ve
./ve/bin/pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

Populate the `media/mathplayground` directory for front-end code.
```
cp -r ~/public_html/mathplayground/public/* ./media/mathplayground/
```
