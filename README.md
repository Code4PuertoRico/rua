![Logo](https://raw.github.com/rosarior/rua/master/rua/docs/_static/rua_logo.png)

RUA
===
RUA (Registro Unico de Agencias) #HackPR


To install
----------
git clone git://github.com/rosarior/rua.git

cd rua

virtualenv venv

source venv/bin/activate

pip install -r rua/requirements/production.txt

./manage.py syncdb --migrate


Create a settings\_local.py file:
---------------------------------
    DEBUG=True

    DEVELOPMENT=True


Execute
---------------------------------
    ./manage.py runserver





* Add data at 127.0.0.1:8000/admin

* API is at 127.0.0.1:8000/api


Examples
--------
![Logo](https://raw.github.com/rosarior/rua/master/rua/docs/_static/single_agency_example.png)
