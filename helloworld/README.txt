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

Example login:
username: gklotz
password: greg 

********************CREATIVITY ELEMENT***********************
All previous user functions have been enhanced with an actual database.
The web application is no longer relient on being a one session run, because
it can now update and query the database for information.

When adding a new user it will check/notify the user if the username is not 
avalible. 

The queries have the MySQL keyword BINARY in them to check if the usernames
and passwords match for case sensitivity because the default for MySQL is 
case-insensitive which could create many issues.

I have updated my Lab History page to include a screenshot from Labs 2 and 3
of what the UI used to look like.

This time around I am making the user use usernames to search for users instead
of having to know the id of the user.

To prevent SQL injections I set up my queries to be first concatednated with the user
entered information. Then I used that SQL variable to be executed.

Authenticaion is also used when trying to edit a user. 

I am using SQL's NOW() function to capture what date the accounts were created on.

Using mako templating to serve up the proper tools. (login, user management)
Added a log in as label and log out button, that deletes the cookie.

Using AJAX to detemine if the user is already logged in via cookies.
***************************************************************