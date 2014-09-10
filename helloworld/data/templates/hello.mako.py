# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1410209623.376648
_enable_loop = True
_template_filename = '/home/undergrad/0/lwong01/Documents/CIS3210/lab1/helloworld/helloworld/templates/hello.mako'
_template_uri = '/hello.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'Hello World, the environ variable looks like: <br />\n')
        # SOURCE LINE 2
        __M_writer(escape(request.environ))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


