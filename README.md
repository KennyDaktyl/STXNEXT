# STXNEXT
Install local info

virtualenv -p python3.8 env
souerce enb/bin/activate
pip freeze -r requrements.txt
psql -h localhost -p postgres

(in postgres create database)
create database stxnext;
(\q; quit from postgres)

(run app)
pyhton manage.py migrate
pyhton manage.py makemigrations
pyhton manage.py runserver

Production info
work on VPS
http//:51.75.127.94:8000/load_data/
(in this view you can paste the link with dataset)
(app create or update new books, attributes and values)
(i try create elastic structure in database, but it is not work correctly, becouse deadline and my actuall job kill my project)

http//:51.75.127.94:8000/db/
(this view get request argument body {"q":"war"} and filter my books collections and response result)
(it work correct, a tested this by POSTMAN)

(i hope than my project is interesting and yuo get me feedback)
(i didn't have many time in this week becouse a work for 8AM to 6PM)
(maybe when i was more time :) ?)

http//:51.75.127.94:8000/db/


