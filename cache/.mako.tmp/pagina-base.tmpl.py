# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1526136317.7009156
_enable_loop = True
_template_filename = 'themes/custom/templates/pagina-base.tmpl'
_template_uri = 'pagina-base.tmpl'
_source_encoding = 'utf-8'
_exports = ['contenido', 'encabezado_extra', 'extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def encabezado_extra():
            return render_encabezado_extra(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def contenido():
            return render_contenido(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contenido(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def contenido():
            return render_contenido(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_encabezado_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def encabezado_extra():
            return render_encabezado_extra(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def encabezado_extra():
            return render_encabezado_extra(context)
        parent = context.get('parent', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n  ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n  ')
        runtime._include_file(context, 'includes/encabezado.tmpl', _template_uri)
        __M_writer('\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'encabezado_extra'):
            context['self'].encabezado_extra(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def contenido():
            return render_contenido(context)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('  <div class="container padding-top margin-bottom">\n    <div class="row">\n      <div class="col-sm-8 col-sm-offset-2">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contenido'):
            context['self'].contenido(**pageargs)
        

        __M_writer('\n      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/pagina-base.tmpl", "uri": "pagina-base.tmpl", "source_encoding": "utf-8", "line_map": {"64": 20, "115": 13, "70": 8, "76": 8, "77": 10, "83": 5, "57": 18, "27": 0, "92": 5, "93": 6, "94": 6, "95": 7, "96": 7, "101": 10, "41": 3, "107": 13, "46": 11, "51": 24, "116": 15, "121": 20, "127": 121, "63": 18}}
__M_END_METADATA
"""
