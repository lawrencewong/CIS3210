README.txt

Lawrence Wong 0725315
CIS*3210

This is the readme file for my application for the computer networking course.
As of right now it is a simple web page that uses jquery and javascript to animate
Links The Cat to do various things through the use of the three buttons provided!

In the root directory start the service by entering the command:

paster serve --reload development.ini

Go to this address in your web browser.
http://127.0.0.1:5000/

I made a web application that pretends there is a working database plugged in. 
It is an application that lets users to be added, edited, checked or removed.
Using different types of requests and actions the server side will return JSON
objects that represent the actions.

********************CREATIVITY ELEMENT***********************
On one session of using the web application the buttons and functions
all work and the server side mimics a plugged in database. Newly created users
can be searched and edited as well as removed. They are assigned 'unique' IDs
based on a counter, to abstract the missing autoincrement of an actual databse.

Styling has improved since the last iteration of the site. A new background image
is set as well as a favicon.

*************************************************************