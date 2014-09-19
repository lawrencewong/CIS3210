import logging
import json

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

log = logging.getLogger(__name__)

user1 = {'id': '1', 'firstname' : 'Lawrence', 'lastname' : 'Wong', 'role' : 'Developer'}
user2 = {'id': '2', 'firstname' : 'Greg', 'lastname' : 'Klotz', 'role' : 'Professor'}
user3 = {'id': '3', 'firstname' : 'Links', 'lastname' : 'Cat', 'role' : 'Feline'}    
data = {
	  '1' : user1,
	  '2' : user2,
	  '3' : user3
	}
userCount = 3;
class UsersController(BaseController):
    
    def addUser(self):
    	if request.method == 'POST':
    		global userCount
    		global data
    		userCount+=1
    		newUser = {'id' : userCount, 'firstname' : request.POST.get('firstName'), 'lastname' : request.POST.get('lastName'), 'role' : 'Guest'}
    		data[userCount] = newUser
    		return json.dumps(newUser)
	  
    def changeName(self, userid):
      c.userid = userid
      if request.method == 'PUT':
		if userid in data:
			data[userid]['firstname'] = request.POST.get('firstName')
			data[userid]['lastname'] = request.POST.get('lastName')
			return json.dumps(data[userid]) 
		else:
			return json.dumps({'error':'User not found.'})
      
    def userCheck(self, userid):
      c.userid = userid
      global data
      if request.method == 'GET':
		if userid in data:
		  return json.dumps(data[userid])
		else:
 		  return json.dumps({'error':'Cannot check for user. User ID not found.'})

      
    def removeUser(self, userid):
		c.userid = userid
		if request.method == 'DELETE':
			if userid in data:
				deleteUser = data[userid]	
				del data[userid]
				return json.dumps(deleteUser)
			else:
				return json.dumps({'error':'Cannot remove user. User not found.'})
