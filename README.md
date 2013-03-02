rua
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

create a settings\_local.py file:
================================
DEBUG=True
DEVELOPMENT=True

execute
=======
./manage.py runserver

add data at 127.0.0.1:8000/admin
API is at 127.0.0.1:8000/api



