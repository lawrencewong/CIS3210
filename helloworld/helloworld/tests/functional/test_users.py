from helloworld.tests import *

class TestUsersController(TestController):

    def test_index(self):
	#Test userCheck
	response = self.app.get(url(controller='users', action='userCheck', userid='1'))
	print response
	assert "id" in response
	assert "1" in response
	
	#Test addUser
	payload = {'firstName' : 'Han', 'lastName' : 'Solo'}
	print payload
	response = self.app.post(url(controller='users', action='addUser'), params=payload)
	print response
	assert "Han" in response
	
	#Test changeName
	payload = {'firstName' : 'Princess', 'lastName' : 'Leia'}
	print payload
	response = self.app.put(url(controller='users', action='changeName', userid='2'), params=payload)
	print response
	assert "2" in response
	assert "Princess" in response
	
	#Test removeUser
	response = self.app.delete(url(controller='users', action='removeUser', userid='3'))
	print response
	assert "id" in response
	assert "3" in response