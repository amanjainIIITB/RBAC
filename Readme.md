# Role Based Access Control:

  A Simple role based auth system. System should be able to assign a role to a user and remove a role from a user.

Entities are USER, ACTION TYPE, RESOURCE, ROLE

ACTION TYPE defines the access level (Ex: READ, WRITE, DELETE)

Access to resources for users are controlled strictly by the role. One user can have multiple roles. Given a user, action type and resource, the system should be able to tell whether user has access or not.


## Installation

```
$ Virtualenv env -p python3
$ source ~/env/bin/activate
$ pip install -r requirement.txt
```

## Run All UnitTestCase

```
$ Virtualenv env -p python3
$ source ~/env/bin/activate
$ python -m unittest discover test
```

## Run Single UnitTestCase

```
$ Virtualenv env -p python3
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

## Run Program

 - cd RBAC/src
 - python RBAC.py, follow the instructions given on the terminal

