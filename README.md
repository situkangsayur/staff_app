# staff_app
Sample app for staff

How to run
---
install virtualenv in your os:
(pip)
```
pip install virtualenv
```

Create virtual env using this command : 
```bash
virtualenv -p python3 venv
```
activate the virtual env:
```bash
. venv/bin/activate
```

yang dibutuhkan : 
    * python3
    * flask
    * flask_restx
    * flask_mongoengine
    * mongodb (install mongodb server)

install libs :
```
pip install flask
pip install flask_restx
pip install flask_mongoengine
```

mongodb installation : https://docs.mongodb.com/manual/installation/

edit file venv/bin/active to add flask main file in the end of file:
```bash
export FLASK_APP=./app/__init__.py
```

deactive virtualenv :
```
deactive
```

lalu aktifkan kembali
```
. venv/bin/activate
```
then run flask command :
 ```bash
 flask run
 ```

