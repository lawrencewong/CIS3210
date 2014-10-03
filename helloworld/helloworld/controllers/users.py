import logging
import json
import MySQLdb

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

log = logging.getLogger(__name__)

#Hardcoded data to simulate a databse of users
#user1 = {'id': '1', 'firstname' : 'Lawrence', 'lastname' : 'Wong', 'role' : 'Developer'}
#user2 = {'id': '2', 'firstname' : 'Greg', 'lastname' : 'Klotz', 'role' : 'Professor'}
#user3 = {'id': '3', 'firstname' : 'Links', 'lastname' : 'Cat', 'role' : 'Feline'}    
#data = {
	  #'1' : user1,
	  #'2' : user2,
	  #'3' : user3
#}
#userCount = 3

db = MySQLdb.connect(host="dursley.socs.uoguelph.ca",
                    user="lwong01", # replace with your username
                    passwd="0725315", # replace with your password (student id number, including leading 0)
                    db="lwong01") # course databasey
cur = db.cursor()
class UsersController(BaseController):
    
    #addUser function adds to the dictionary of users incrementing the userCount for 'unique' ID's. Utilizing POST request.
	def addUser(self):
		data = 0;
		if request.method == 'POST':
			cur.execute('INSERT INTO users VALUES (NULL, "' + request.POST.get('firstName') + '", "' + request.POST.get('lastName') + '", "' + request.POST.get('dateOfBirth') + '", "' + request.POST.get('userName') + '", "' + request.POST.get('password') + '");')
			db.commit()
			cur.execute('SELECT * FROM users WHERE username = "' + request.POST.get('userName') +'";')
			for row in cur.fetchall() :
			  data = {
			    'id': row[0],
			    'firstname' : row[1],
			    'lastname' : row[2],
			    'date_of_birth' : row[3].isoformat() if hasattr(row[3], 'isoformat') else row[3],
			    'username' : row[4]
			  }
			return json.dumps(data)

	#changeName changes the first and last name of a give user ID. Using PUT requests.
	def editUser(self):
		data = 0;
		if request.method == 'PUT':
			cur.execute('SELECT * FROM users WHERE username = "' + request.POST.get('userName') + '" AND password = "' + request.POST.get('password') + '";')
			for row in cur.fetchall() :
			  data = {
			    'id': row[0],
			    'firstname' : row[1],
			    'lastname' : row[2],
			    'date_of_birth' : row[3].isoformat() if hasattr(row[3], 'isoformat') else row[3],
			    'username' : row[4]
			  }
			if data:
				cur.execute('UPDATE users SET firstname = "' + request.POST.get('firstName') + '",  lastname= "' + request.POST.get('lastName') + '", date_of_birth = "' + request.POST.get('dateOfBirth') + '";')
				db.commit()
				cur.execute('SELECT * FROM users WHERE id = "' + data['id'] + '";')
				for row in cur.fetchall() :
				  data = {
				    'id': row[0],
				    'firstname' : row[1],
				    'lastname' : row[2],
				    'date_of_birth' : row[3].isoformat() if hasattr(row[3], 'isoformat') else row[3],
				    'username' : row[4]
				  }
				return json.dumps(data)
			else:
				return json.dumps({'error':'Authentication error.'})

	#userCheck function to look up a given user based on user ID. Using GET requests.
	def userCheck(self, userid):
		c.userid = userid
		data = 0;
		if request.method == 'GET':
		  cur.execute('SELECT * FROM users WHERE id = "' + userid +'";')
		  for row in cur.fetchall() :
		    data = {
		      'id': row[0],
		      'firstname' : row[1],
		      'lastname' : row[2],
		      'date_of_birth' : row[3].isoformat() if hasattr(row[3], 'isoformat') else row[3],
		      'username' : row[4]
		    }
		  if data:
			  return json.dumps(data)
		  else:
			  return json.dumps({'error':'Cannot check for user. User ID not found.'})

	#remoceUser deletes a user from the 'database' based on user ID. Using DELETE requests.
	def removeUser(self, userid):
		data = 0;
		if request.method == 'DELETE':
		      cur.execute('SELECT * FROM users WHERE id = "' + userid +'";')
		      for row in cur.fetchall() :
			data = {
			  'id': row[0],
			  'firstname' : row[1],
			  'lastname' : row[2],
			  'date_of_birth' : row[3].isoformat() if hasattr(row[3], 'isoformat') else row[3],
			  'username' : row[4]
			}
		      cur.execute('DELETE FROM users WHERE id = "' + userid +'";')
		      db.commit()
		      if data:
			      return json.dumps(data)
		      else:
			      return json.dumps({'error':'Cannot remove user. User not found.'})
