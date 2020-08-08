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
http://51.75.127.94:8000/load_data/<br />
<br />
(in this view you can paste the link with dataset)<br />
(app create or update new books, attributes and values)<br />
(i try create elastic structure in database, but it is not work correctly, becouse my current job takes a lot of my time)<br />
<br />
http://51.75.127.94:8000/books/<br />
<br />
(i used framework django restframework and django filters)
(for check book details use exist ID for example [113,114,....122])
http://51.75.127.94:8000/books/113<br />
<br />
http://51.75.127.94:8000/db/<br />
<br />
(this view get request argument body {"q":"war"} and filter my books collections and response result)<br />
(it work correct, a tested this by POSTMAN)<br />
<br />
http://51.75.127.94:8000/admin<br />
StxNextPoznan
stxnext123
<br />
(i hope than my project is interesting and you get me feedback for next knowledge. Can I ask you to solve the problem correctly in order to continue my learning. Thanks for that :))
(i didn't have many time in this week becouse i send in my job from 8AM to 6PM)
(maybe when i had more time i was the Best :) ?)




