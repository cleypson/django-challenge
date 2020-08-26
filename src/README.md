# Run the project with docker-compose (Linux)

On the terminal run (can be VSCode Terminal):
```
cd solution
make build
make up
```

- Make sure of the ports be open: 8100:5434:3000

In a new tab run followings command:

```
make migrate
```
at last in the same tab run:
```
make test
```

# Run the project without docker-compose (Linux)

On the terminal run (can be VSCode Terminal):
```
cd solution
virtualenv -p python3 .venv/
source solution/.venv/bin/activate
cd src
pip install -r requirements.txt
```

Now we change the DATABASE=default for sqlite3:

in development.py comment out the following lines like this:

```
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'django_challenge',
#        'USER': 'django_challenge',
#        'PASSWORD': 'GT8XmPY2xvENgpGz',
#        'HOST': 'db',
#        'PORT': '5432',
#    }
#}
```

Now we can run the migrate command

```
python manage.py migrate
```

with this we can run and test the project

```
python manage.py runserver 0.0.0.0:8000
```
or
```
python manage.py test
```

About the API:

| URL                     |  Method   | Params  | Description          |
|-------------------------|:---------:|:--------|----------------------|
| /api/v1/signup/         |    POST   | { 'email': 'test@example.com',<br/>'password': 'password' }   | Sign up user        |
| /api/v1/login/          |    POST   | { 'email': 'test@example.com',<br/>'password': 'password' }   | Login as user(Get the token)       |
| /api/v1/cars/           |    POST   |    -    | List all cars        |
| /api/v1/cars/           |    POST   |    -    | List all cars        |
| /api/v1/projects/       |    GET    |    -    | List all nevers      |
| /api/v1/nevers/         |    GET    |    -    | List all projects    |
| /api/v1/projects/{id}   |    GET    |{'name': 'Projeto Payload' }    | Add one project  |
| /api/v1/nevers/{id}     |    GET    |    {'name': 'Never Payload', <br/>'birthdate': '01/01/2004', <br/>'admission_date': '01/05/2016', <br/>'job_role': 'DBA'}   | Add one never     |
