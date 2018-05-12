# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1526136317.9638062
_enable_loop = True
_template_filename = '/home/ela/entornos/pyecEnv/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_intensedebate.tmpl'
_template_uri = 'comments_helper_intensedebate.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link_script', 'comment_form', 'comment_link']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\n<script>\nvar idcomments_acct = '")
        __M_writer(str(comment_system_id))
        __M_writer('\';\nvar idcomments_post_id = "')
        __M_writer(str(identifier))
        __M_writer('";\nvar idcomments_post_url = "')
        __M_writer(str(url))
        __M_writer('";\n</script>\n<span id="IDCommentsPostTitle" style="display:none"></span>\n<script src=\'http://www.intensedebate.com/js/genericCommentWrapperV2.js\'></script>\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<a href="{link}" onclick="this.href=\'')
        __M_writer(str(link))
        __M_writer('\'; this.target=\'_self\';"><span class=\'IDCommentsReplace\' style=\'display:none\'>')
        __M_writer(str(identifier))
        __M_writer("</span>\n<script>\nvar idcomments_acct = '")
        __M_writer(str(comment_system_id))
        __M_writer('\';\nvar idcomments_post_id = "')
        __M_writer(str(identifier))
        __M_writer('";\nvar idcomments_post_url = "')
        __M_writer(str(link))
        __M_writer('";\n</script>\n<script src="http://www.intensedebate.com/js/genericLinkWrapperV2.js"></script>\n</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ela/entornos/pyecEnv/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_intensedebate.tmpl", "uri": "comments_helper_intensedebate.tmpl", "source_encoding": "utf-8", "line_map": {"64": 14, "65": 14, "66": 16, "67": 16, "68": 17, "69": 17, "70": 18, "71": 18, "77": 71, "16": 0, "21": 11, "22": 22, "23": 25, "29": 24, "33": 24, "39": 2, "44": 2, "45": 4, "46": 4, "47": 5, "48": 5, "49": 6, "50": 6, "56": 13, "61": 13, "62": 14, "63": 14}}
__M_END_METADATA
"""
