# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1526136317.3706133
_enable_loop = True
_template_filename = '/home/ela/entornos/pyecEnv/lib/python3.5/site-packages/nikola/data/themes/bootstrap3/templates/listing.tmpl'
_template_uri = 'listing.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def content():
            return render_content(context._locals(__M_locals))
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def sourcelink():
            return render_sourcelink(context)
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if source_link:
            __M_writer('    <li>\n    <a href="')
            __M_writer(str(source_link))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def content():
            return render_content(context)
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\n')
        if folders or files:
            __M_writer('<ul>\n')
            for name in folders:
                __M_writer('    <li><a href="')
                __M_writer(filters.url_escape(str(name)))
                __M_writer('"><i class="glyphicon glyphicon-folder-open"></i> ')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a>\n')
            for name in files:
                __M_writer('    <li><a href="')
                __M_writer(filters.url_escape(str(name)))
                __M_writer('.html"><i class="glyphicon glyphicon-file"></i> ')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a>\n')
            __M_writer('</ul>\n')
        if code:
            __M_writer('<h1>')
            __M_writer(str(title))
            __M_writer('\n')
            if source_link:
                __M_writer('        <small><a href="')
                __M_writer(str(source_link))
                __M_writer('">(')
                __M_writer(str(messages("Source")))
                __M_writer(')</a></small>\n')
            __M_writer('    </h1>\n    ')
            __M_writer(str(code))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ela/entornos/pyecEnv/lib/python3.5/site-packages/nikola/data/themes/bootstrap3/templates/listing.tmpl", "uri": "listing.tmpl", "source_encoding": "utf-8", "line_map": {"128": 19, "129": 19, "130": 19, "131": 21, "132": 22, "133": 22, "139": 133, "23": 3, "29": 0, "48": 2, "49": 3, "54": 24, "59": 32, "65": 26, "75": 26, "76": 27, "77": 28, "78": 29, "79": 29, "80": 29, "81": 29, "87": 4, "103": 4, "104": 5, "105": 5, "106": 6, "107": 7, "108": 8, "109": 9, "110": 9, "111": 9, "112": 9, "113": 9, "114": 11, "115": 12, "116": 12, "117": 12, "118": 12, "119": 12, "120": 14, "121": 16, "122": 17, "123": 17, "124": 17, "125": 18, "126": 19, "127": 19}}
__M_END_METADATA
"""
