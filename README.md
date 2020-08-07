# STXNEXT
Install local info

virtualenv -p python3.8 env<br />
source enb/bin/activate<br />
pip freeze -r requrements.txt<br />
psql -h localhost -p postgres<br />

(in postgres create database)<br />
create database stxnext;<br />
(\q; quit from postgres)<br />
<br />
(run app)<br />
pyhton manage.py migrate<br />
pyhton manage.py makemigrations<br />
pyhton manage.py runserver<br />
<br />
Production info<br />
work on VPS<br />
<br />
http//:51.75.127.94:8000/load_data/<br />
<br />
(in this view you can paste the link with dataset)<br />
(app create or update new books, attributes and values)<br />
(i try create elastic structure in database, but it is not work correctly, becouse deadline and my actuall job kill my project)<br />
<br />
http//:51.75.127.94:8000/db/<br />
<br />
(this view get request argument body {"q":"war"} and filter my books collections and response result)<br />
(it work correct, a tested this by POSTMAN)<br />

(i hope than my project is interesting and yuo get me feedback for next knowledge. I want to get info about 100% working code for my new skill. Thanks for that :))
(i didn't have many time in this week becouse a work for 8AM to 6PM)
(maybe when i was more time :) ?)




