# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1526136318.098184
_enable_loop = True
_template_filename = '/home/ela/entornos/pyecEnv/lib/python3.5/site-packages/nikola/data/themes/base/templates/archive_navigation_helper.tmpl'
_template_uri = 'archive_navigation_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['archive_navigation']


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


def render_archive_navigation(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        pagekind = context.get('pagekind', UNDEFINED)
        next_archive = context.get('next_archive', UNDEFINED)
        up_archive = context.get('up_archive', UNDEFINED)
        previous_archive = context.get('previous_archive', UNDEFINED)
        has_archive_navigation = context.get('has_archive_navigation', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'archive_page' in pagekind:
            if has_archive_navigation:
                __M_writer('        <nav class="archivenav">\n        <ul class="pager">\n')
                if previous_archive:
                    __M_writer('            <li class="previous"><a href="')
                    __M_writer(str(previous_archive))
                    __M_writer('" rel="prev">')
                    __M_writer(str(messages("Previous")))
                    __M_writer('</a></li>\n')
                else:
                    __M_writer('            <li class="previous disabled"><a href="#" rel="prev">')
                    __M_writer(str(messages("Previous")))
                    __M_writer('</a></li>\n')
                if up_archive:
                    __M_writer('            <li class="up"><a href="')
                    __M_writer(str(up_archive))
                    __M_writer('" rel="up">')
                    __M_writer(str(messages("Up")))
                    __M_writer('</a></li>\n')
                else:
                    __M_writer('            <li class="up disabled"><a href="#" rel="up">')
                    __M_writer(str(messages("Up")))
                    __M_writer('</a></li>\n')
                if next_archive:
                    __M_writer('            <li class="next"><a href="')
                    __M_writer(str(next_archive))
                    __M_writer('" rel="next">')
                    __M_writer(str(messages("Next")))
                    __M_writer('</a></li>\n')
                else:
                    __M_writer('            <li class="next disabled"><a href="#" rel="next">')
                    __M_writer(str(messages("Next")))
                    __M_writer('</a></li>\n')
                __M_writer('        </ul>\n        </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ela/entornos/pyecEnv/lib/python3.5/site-packages/nikola/data/themes/base/templates/archive_navigation_helper.tmpl", "uri": "archive_navigation_helper.tmpl", "source_encoding": "utf-8", "line_map": {"64": 19, "65": 19, "66": 19, "67": 19, "68": 20, "69": 21, "70": 21, "71": 21, "72": 23, "78": 72, "16": 0, "21": 2, "22": 27, "28": 3, "38": 3, "39": 4, "40": 5, "41": 6, "42": 8, "43": 9, "44": 9, "45": 9, "46": 9, "47": 9, "48": 10, "49": 11, "50": 11, "51": 11, "52": 13, "53": 14, "54": 14, "55": 14, "56": 14, "57": 14, "58": 15, "59": 16, "60": 16, "61": 16, "62": 18, "63": 19}}
__M_END_METADATA
"""
