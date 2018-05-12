# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1526136318.0055869
_enable_loop = True
_template_filename = '/home/ela/entornos/pyecEnv/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_facebook.tmpl'
_template_uri = 'comments_helper_facebook.tmpl'
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
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div id="fb-root"></div>\n<script>\n    // thank lxml for this\n    $(\'.fb-comments-count\').each(function(i, obj) {\n        var url = obj.attributes[\'data-url\'].value;\n        // change here if you dislike the default way of displaying\n        // this\n        obj.innerHTML = \'<fb:comments-count href="\' + url + \'"></fb:comments-count> comments\';\n    });\n\n  window.fbAsyncInit = function() {\n    // init the FB JS SDK\n    FB.init({\n      appId      : \'')
        __M_writer(str(comment_system_id))
        __M_writer('\',\n      status     : true,\n      xfbml      : true\n    });\n\n  };\n\n  // Load the SDK asynchronously\n  (function(d, s, id){\n     var js, fjs = d.getElementsByTagName(s)[0];\n     if (d.getElementById(id)) {return;}\n     js = d.createElement(s); js.id = id;\n     js.src = "https://connect.facebook.net/en_US/all.js";\n     fjs.parentNode.insertBefore(js, fjs);\n   }(document, \'script\', \'facebook-jssdk\'));\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div id="fb-root"></div>\n<script>\n  window.fbAsyncInit = function() {\n    // init the FB JS SDK\n    FB.init({\n      appId      : \'')
        __M_writer(str(comment_system_id))
        __M_writer('\',\n      status     : true,\n      xfbml      : true\n    });\n\n  };\n\n  // Load the SDK asynchronously\n  (function(d, s, id){\n     var js, fjs = d.getElementsByTagName(s)[0];\n     if (d.getElementById(id)) {return;}\n     js = d.createElement(s); js.id = id;\n     js.src = "https://connect.facebook.net/en_US/all.js";\n     fjs.parentNode.insertBefore(js, fjs);\n   }(document, \'script\', \'facebook-jssdk\'));\n</script>\n\n<div class="fb-comments" data-href="')
        __M_writer(str(url))
        __M_writer('" data-width="470"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n<span class="fb-comments-count" data-url="')
        __M_writer(str(link))
        __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ela/entornos/pyecEnv/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_facebook.tmpl", "uri": "comments_helper_facebook.tmpl", "source_encoding": "utf-8", "line_map": {"48": 8, "34": 32, "35": 46, "36": 46, "69": 63, "42": 2, "61": 28, "47": 2, "16": 0, "49": 8, "50": 25, "51": 25, "21": 26, "22": 30, "23": 62, "57": 28, "29": 32, "62": 29, "63": 29}}
__M_END_METADATA
"""
