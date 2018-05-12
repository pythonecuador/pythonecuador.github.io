# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1526136320.2234643
_enable_loop = True
_template_filename = 'themes/custom/templates/includes/encabezado.tmpl'
_template_uri = 'includes/encabezado.tmpl'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n\n')
        __M_writer('<link rel="stylesheet" href="/assets/css/custom.css" type="text/css" media="all" />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/includes/encabezado.tmpl", "uri": "includes/encabezado.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "29": 23, "21": 2, "22": 4, "23": 7}}
__M_END_METADATA
"""
