![Logo](https://github.com/rosarior/rua/raw/master/docs/_static/rua_logo.png)

RUA
===
RUA (Registro Unico de Agencias) #HackPR


To install
==========
git clone git://github.com/rosarior/rua.git

cd rua

virtualenv venv

source venv/bin/activate

pip install requirements/production.txt

./manage.py syncdb --migrate


Create a settings\_local.py file:

    DEBUG=True
    
    DEVELOPMENT=True

Execute
~~~~~~~
./manage.py runserver

add data at 127.0.0.1:8000/admin

API is at 127.0.0.1:8000/api
