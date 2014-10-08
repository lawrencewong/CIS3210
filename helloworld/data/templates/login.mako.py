# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1412798740.70595
_enable_loop = True
_template_filename = '/home/undergrad/0/lwong01/Documents/CIS3210/lab2/CIS3210/helloworld/helloworld/templates/login.mako'
_template_uri = '/login.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<div class="container">\n\t<h1 style="font-size: 75px;">Hi there.</h1>\n\t<div class="rest-form">\n\t  <div class="row">\n\t    <div class="span12">\n\t      <h3>Log in</h3>\n\t      <div>\n\t\t<input type="text" id="userName" placeholder="Username">\n\t      </div>\n\t      <div>\n\t\t<input type="password" id="password" placeholder="Password">\n\t      </div>\n\t      <div>\n\t\t<button class="btn btn-info btn-small" id="Submit">Submit</button>\n\t      </div>\n\t    </div>\n\t  </div>\n\t</div>\n      </div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


