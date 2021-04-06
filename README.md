# Django-Learning


## Getting Started (For Linux)

#### Global Install from Packages
If you wish to install Django using the Ubuntu repositories, the process is very straightforward.

First, update your local package index with apt:
```bash
$ sudo apt update
```

Next, check which version of Python you have installed.
```bash
$ python3 -V
```

Next, install Django:
```bash
$ sudo apt install python3-django
```

You can test that the installation was successful by typing:
```bash
$ django-admin --version
```
```bash
Output
1.11.11
```

## Creating First Project

You can view all the options for usage of django using
```bash
$ django-admin
```
To create a project :
```bash
$ django-admin startproject <project_name> .
```
The " . " is such that if you are inside a perticular folder like "src" then manage.py applies to the whole folder also

**Note:** The name of the project should not match with the other predefined options as of django-admin

To run the server :
```bash
$ python3 manage.py runserver
```
Then you will see output like this -
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 06, 2021 - 05:22:50
Django version 2.2.16, using settings 'first_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Go to the server mentioned for the Django startup page

For migration :
```bash
$ python3 manage.py migrate
```
This will sync all the current components, settings and other with the django project
