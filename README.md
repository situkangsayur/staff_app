# staff_app
Sample app for staff
How to run

install virtualenv in your os:
(pip)
```
pip install virtualenv
```
Create virtual env using this command : 
```bash
virtualenv -p python3 venv
```
edit file venv/bin/active to add flask main file in the end of file:
```bash
export FLASK_APP=./app/__init__.py
```

activate the virtual env:
```bash
. venv/bin/activate
```

then run flask command :
 ```bash
 flask run
 ```
