# Role Based Access Control:

  A Simple role based auth system. System should be able to assign a role to a user and remove a role from a user.

Entities are USER, ACTION TYPE, RESOURCE, ROLE

ACTION TYPE defines the access level (Ex: READ, WRITE, DELETE)

Access to resources for users are controlled strictly by the role. One user can have multiple roles. Given a user, action type and resource, the system should be able to tell whether user has access or not.


## Run Application without Docker in Production

```
$ Virtualenv env -p python2
$ source ~/env/bin/activate
$ pip install -r requirement.txt
$ python src/RBAC.py
```

## Run Application without Docker in Debug Mode

```
$ Virtualenv env -p python2
$ source ~/env/bin/activate
$ pip install -r requirement.txt
$ python src/RBAC.py --debug
```

## Run Application with Docker in Production

```
$ docker build -t python-rbac .
$ docker run -ti python-rbac
```

## Run Application with Docker in Debug mode

```
$ docker build -t python-rbac .
$ docker run -ti python-rbac python /src/RBAC.py --debug
```

## Run All UnitTestCase

```
$ Virtualenv env -p python2
$ source ~/env/bin/activate
$ python -m unittest discover test
```

## Run Single UnitTestCase

```
$ Virtualenv env -p python2
$ source ~/env/bin/activate
$ python -m unittest test.filename
```

 
## Operations Allowed

 - Login User to the System
 - Create User Account
 - View the list of Roles Supported by the System
 - Check whether user has access or not.
 - Assign Role to the User
 - Revoke Role from the User