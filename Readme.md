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
