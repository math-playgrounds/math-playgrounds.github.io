# mathplayground_django
Django Channels server for mathplayground

## Start-up steps:
Start redis:
```
docker run -p 6379:6379 -d redis:5
```

Start django server:
```
python3 -m venv ve
./ve/bin/pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```