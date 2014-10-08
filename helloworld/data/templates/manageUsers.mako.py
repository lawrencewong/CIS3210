# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1412798027.024401
_enable_loop = True
_template_filename = '/home/undergrad/0/lwong01/Documents/CIS3210/lab2/CIS3210/helloworld/helloworld/templates/manageUsers.mako'
_template_uri = '/manageUsers.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<div class="container">\n        <h2><a href="http://www.mysql.com/" style="color: #000000;">MySQL</a></h2>\n\t<h5>This is an web application that uses a RESTful API and jQuery\'s AJAX to mimic a user managment web application with a database.\n\t    Play with the user\'s functions and see what the returns from the server side are. All user functions work. The server side has been\n\t    updated to work with a running MySQL databse.\n\t</h5>\n      </div>\n\n      <div class="container">\n        <div class="rest-form">\n          <div class="row">\n            <div class="span6">\n              <div>\n                <input type="text" id="userName" placeholder="Username">\n              </div>\n              <div>\n                <input type="password" id="password" placeholder="Password">\n              </div>\n              <div>\n                <input type="text" id="firstName" placeholder="First Name">\n              </div>\n              <div>\n                <input type="text" id="lastName" placeholder="Last Name">\n              </div>\n            </div>\n            <div class="span6">\n              <label for="status-box" class="rest-labels">User Functions:</label>\n              <div>\n                <button class="btn btn-success btn-small" id="addUser">Add User</button>\n                <button class="btn btn-warning btn-small" id="changeName">Edit User</button>\n                <button class="btn btn-info btn-small" id="checkUser">User Check</button>\n                <button class="btn btn-danger btn-small" id="removeUser">Remove User</button>\n              </div>\n            </div>\n          </div>\n        </div>\n      </div>\n\n      <div class="user-forms">\n        <label for="status-box"  class="rest-labels">Status / Returns:</label>\n        <textarea readonly id="status-box" placeholder="Status and data that will be returned."></textarea>\n      </div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


