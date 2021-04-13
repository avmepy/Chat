## Simple chat room implementation using django-rest

#### 1. test-version sqlite3 heroku

https://chatmsgapp.herokuapp.com

superuser:
username: admin
password: admin


### endpoints

admin panel
https://chatmsgapp.herokuapp.com/admin/

login
https://chatmsgapp.herokuapp.com/api/login/

logout
https://chatmsgapp.herokuapp.com/api/logout/

register (post)
https://chatmsgapp.herokuapp.com/api/auth/users/

list of messages paginated by 10
(for example 1)
https://chatmsgapp.herokuapp.com/api/messages/list/1/

create new message
https://chatmsgapp.herokuapp.com/api/messages/create/

read/update/delete message
(by its id, 1 for example)
https://chatmsgapp.herokuapp.com/api/messages/single/1/



#### 2. heroku postgres 

https://chatmsgwithpostgresapp.herokuapp.com

superuser:
username: admin
password: admin

the same endpoints (excluding host)



## installation


project:

open terminal

```git clone https://github.com/avmepy/Chat.git```

```cd Chat```

```python3 -m pip install --user virtualenv```

```python3 -m venv env```

```source env/bin/activate```

```pip install -r requirements.txt```

database:

docker and macOS in my case

download docker from
```https://docs.docker.com/docker-for-mac/install/```

then via terminal

```docker pull postgres```

```docker run -e POSTGRES_PASSWORD={tour password} -e POSTGRES_USERNAME={youe username} -it --rm -p 5432:5432 -d --name pg postgres```

```brew install libpq```

```brew link --force libpq ail```

```export PGPASSWORD={your password}```

```export PGUSERMANE={your username}```

```psql -h localhost -U postgres -w```

```CREATE DATABASE pg;```

generate tables:

```python manage.py makemigrations```

```python manage.py migrate```


to create superuser:

```python manage.py cratesuperuser```

to start server:

```python manage.py runserver```
