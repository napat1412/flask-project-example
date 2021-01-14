# flask-project-example
flask-project-example is designed to support OIDC, SQLAlchemy and Blueprint. This project has 2 route path /oidc and /db that register through Blueprint. 
- Routepath /oidc <br>
Route pah /oidc/api is shown OIDC token verification that use for Backend API. <br>
Other route pah /oidc, /oidc/private and /oidc/logout is used for Frontend Login & Logout. <br>

- Routepath /db <br>
Route path [GET]    /db/student is shown List students. <br>
Route path [POST]   /db/student-new is used to create student. <br>
Route path [GET]    /db/student/<student.name> is used to get a student by name. <br>
Route path [DELETE]    /db/student/<student.name> is used to delete a student by name. <br>

## Source
- [Simple python example using flask_oidc and keycloak](https://gist.github.com/thomasdarimont/145dc9aa857b831ff2eff221b79d179a)
- [Flask SQLAlchemy](https://pythonbasics.org/flask-sqlalchemy/)

## Installation
```sh
# virtualenv --python /usr/bin/python3.6
pip install -r requirements.txt
export FLASK_ENV=development
export FLASK_APP=run.py
flask initdb
flask run --host 0.0.0.0
```
