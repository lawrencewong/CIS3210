import logging
import json
import MySQLdb

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

log = logging.getLogger(__name__)

db = MySQLdb.connect(host="dursley.socs.uoguelph.ca",
                    user="lwong01", # replace with your username
                    passwd="0725315", # replace with your password (student id number, including leading 0)
                    db="lwong01") # course databasey
cur = db.cursor()
class UsersController(BaseController):
	
	def index(self):
	  return render("/login.mako");
      
	def test(self):
	  return render("/manageUsers.mako")
	  
	#existingUser checks if there is a user already with the same username
	def existingUser(self, username):
		c.username = username
		if request.method == 'GET':
		  sql = 'SELECT * FROM users WHERE BINARY username = "' + username + '";'
		  cur.execute(sql)
		  row = cur.fetchone()
		  if row:
		    return json.dumps({'error':'Username already exists.'})
		  else:
		    return json.dumps({'success':'Username avaliable.'})
	  
	  
        #addUser function adds to the dictionary of users incrementing the userCount for 'unique' ID's. Utilizing POST request.
	def addUser(self):
		data = 0;
		if request.method == 'POST':
			sql = 'INSERT INTO users VALUES (NULL, "' + request.POST.get('firstName') + '", "' + request.POST.get('lastName') + '", "' + request.POST.get('userName') + '", "' + request.POST.get('password') + '", NOW());'
			cur.execute(sql)
			db.commit()
			sql = 'SELECT * FROM users WHERE BINARY username = "' + request.POST.get('userName') +'";'
			cur.execute(sql)
			row = cur.fetchone()
			if row:
			  data = {
			    'id': row[0],
			    'firstname' : row[1],
			    'lastname' : row[2],
			    'username' : row[3],
			    'acccount_creation_date': row[5].isoformat() if hasattr(row[5], 'isoformat') else row[5]
			  }
			return json.dumps(data)

	#changeName changes the first and last name of a give user ID. Using PUT requests.
	def editUser(self):
		data = 0;
		if request.method == 'PUT':
			sql = 'SELECT * FROM users WHERE BINARY username = "' + request.POST.get('userName') + '" AND BINARY password = "' + request.POST.get('password') + '";'
			cur.execute(sql)
			row = cur.fetchone()
			if row:
				sql = 'UPDATE users SET firstname = "' + request.POST.get('firstName') + '",  lastname= "' + request.POST.get('lastName') + '" WHERE id = "' + str(data['id']) +'";'
				cur.execute(sql)
				db.commit()
				cur.execute('SELECT * FROM users WHERE id = "' + str(data['id']) + '";')
				for row in cur.fetchall() :
				  data = {
				    'id': row[0],
				    'firstname' : row[1],
				    'lastname' : row[2],
				    'username' : row[3],
				    'acccount_creation_date': row[5].isoformat() if hasattr(row[5], 'isoformat') else row[5]
				  }
				return json.dumps(data)
			else:
				return json.dumps({'error':'Authentication error.'})

	#userCheck function to look up a given user based on user ID. Using GET requests.
	def userCheck(self, username):
		c.username = username
		data = 0;
		if request.method == 'GET':
		  sql = 'SELECT * FROM users WHERE BINARY username = "' + username +'";'
		  cur.execute(sql)
		  row = cur.fetchone()
		  if row:
		    data = {
		      'id': row[0],
		      'firstname' : row[1],
		      'lastname' : row[2],
		      'username' : row[3],
		      'acccount_creation_date': row[5].isoformat() if hasattr(row[5], 'isoformat') else row[5]
		    }
		  if data:
			  return json.dumps(data)
		  else:
			  return json.dumps({'error':'Cannot check for user. User not found.'})

	#remoceUser deletes a user from the 'database' based on user ID. Using DELETE requests.
	def removeUser(self, username):
		c.username = username
		data = 0;
		if request.method == 'DELETE':
		      sql = 'SELECT * FROM users WHERE BINARY username = "' + username +'";'
		      cur.execute(sql)
		      row = cur.fetchone()
		      if row:
			data = {
			    'id': row[0],
			    'firstname' : row[1],
			    'lastname' : row[2],
			    'username' : row[3],
			    'acccount_creation_date': row[5].isoformat() if hasattr(row[5], 'isoformat') else row[5]
			  }
			sql = 'DELETE FROM users WHERE username = "' + username +'";'
			cur.execute(sql)
			db.commit()
			if data:
				return json.dumps(data)
		      else:
			      return json.dumps({'error':'Username does not exist.'})
			   
