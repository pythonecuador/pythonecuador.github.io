# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1526136317.4800854
_enable_loop = True
_template_filename = '/home/ela/entornos/pyecEnv/lib/python3.5/site-packages/nikola/data/themes/base/templates/crumbs.tmpl'
_template_uri = 'crumbs.tmpl'
_source_encoding = 'utf-8'
_exports = ['bar']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bar(context,crumbs):
    __M_caller = context.caller_stack._push_frame()
    try:
        index_file = context.get('index_file', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if crumbs:
            __M_writer('<nav class="breadcrumbs">\n<ul class="breadcrumb">\n')
            for link, text in crumbs:
                if text != index_file:
                    if link == '#':
                        __M_writer('                <li>')
                        __M_writer(str(text.rsplit('.html', 1)[0]))
                        __M_writer('</li>\n')
                    else:
                        __M_writer('                <li><a href="')
                        __M_writer(str(link))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a></li>\n')
            __M_writer('</ul>\n</nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ela/entornos/pyecEnv/lib/python3.5/site-packages/nikola/data/themes/base/templates/crumbs.tmpl", "uri": "crumbs.tmpl", "source_encoding": "utf-8", "line_map": {"33": 3, "34": 4, "35": 5, "36": 7, "37": 8, "38": 9, "39": 10, "40": 10, "41": 10, "42": 11, "43": 12, "44": 12, "45": 12, "46": 12, "47": 12, "16": 0, "48": 16, "21": 2, "22": 19, "54": 48, "28": 3}}
__M_END_METADATA
"""
