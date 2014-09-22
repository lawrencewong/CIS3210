from helloworld.tests import *

class TestUsersController(TestController):

    def test_index(self):
	response = self.app.get(url(controller='users', action='userCheck', userid='1'))\
	print response
	assert '"id": "1"' in response
	assert '"firstname" : "Lawrence"' in response
	assert '"lastname" : "Wong"' in response
	assert '"role" : "Developer"' in response