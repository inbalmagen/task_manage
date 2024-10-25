# task_manage
create a basic task app:
1. create virtural envioronment + activate
2. install Django
3. start project . (dot is important!)
4. start app (tasks)
5. settings → INSTALLED APPS
6. models → create task class (Django rest framework model)
7. serializers.py → file + taskserializer
8. views → create @api views functions
9. install Django restframework + INSTALLED APPS
10. create urls.py for tasks 
11. add path to project urls
12. Pip freeze >  requirements.txt
** no migrations made yet!

addin users app
1. create users app + INSTALLED APPS
2. models → custom django user 
3. settings → AUTH_USER_MODEL
4. register admins
6. create superuser
6. makemigrations + migrate
7. runserver
** at this point:
   / all tasks
   /admin/ → tasks, users

1. add tasks 
2. add user to tasks model
3. makemigrations + migrate
4. runserver
** at this point:
   / all tasks + users

1. adding favorite color to user
2. makemigrations, migrate
3. runserver

1. adding endpoints in views.py, urls.py

login:
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation

1. pip install JWT
2. REST_FRAMEWORK =
3. add tokens paths to project urls.py
4. INSTALLED_APPS
5. runserver
6. check in thunder client: POST
   http://127.0.0.1:8000/login/

   {"username":"admin",
   "password":"123"}

   result: refresh token, access token

permissions:
1. @permission_classes([IsAuthenticated])
2. from rest_framework.decorators import api_view, permission_classes
   from rest_framework.permissions import IsAuthenticated
3. check in thunder client: GET
   login to get new access token
   http://127.0.0.1:8000

   Auth → Bearer → past access token
   result: user tasks:
   [
  {
    "id": 1,
    "name": "washe the dishes",
    "deadline": "2024-10-24",
    "done": false,
    "user": 1
  },
  {
    "id": 2,
    "name": "sweep the floor",
    "deadline": "2024-10-25",
    "done": false,
    "user": 1
  }
]



   





   




