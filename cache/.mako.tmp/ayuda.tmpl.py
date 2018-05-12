# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1526136317.6834276
_enable_loop = True
_template_filename = 'themes/custom/templates/ayuda.tmpl'
_template_uri = 'ayuda.tmpl'
_source_encoding = 'utf-8'
_exports = ['contenido']


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
    return runtime._inherit_from(context, 'pagina-base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        post = context.get('post', UNDEFINED)
        def contenido():
            return render_contenido(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contenido'):
            context['self'].contenido(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contenido(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        def contenido():
            return render_contenido(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="alert alert-warning" role="alert">\n    Sección no implementada\n  </div>\n\n  <h2>¡Esta sección necesita de tu ayuda!</h2>\n  <p>\n    Actualmente esta sección no está implementada en el sitio,\n    pero ya que estás interesada/o en esta sección creemos que podrías darnos una mano.\n    Debajo se encuentra una breve descripción de lo que deberías implementar.\n  </p>\n\n  <div class="panel panel-info">\n    <div class="panel-heading">¿Qué debe ir en esta página?</div>\n    <div class="panel-body">\n      ')
        __M_writer(str(post.text()))
        __M_writer('\n    </div>\n  </div>\n\n  <h3>¡Quiero ayudar! ¿Cómo lo hago?</h3>\n  <p>\n    ¡Muchas gracias por el interés en ayudar!\n    El desarrollo de nuestro sitio se lleva a cabo en GitHub sobre este repositorio\n    <a href="https://github.com/PythonEcuador/PythonEcuador.github.io">pythonecuador/pythonecuador.github.io</a>.\n  </p>\n  <p>\n    El sitio es un sitio estático construído con html, css y javascript, y alojado en GitHub Pages.\n    Pero no necesitas saber nada de esto para empezar a colaborar,\n    cualquier tipo de ayuda es muy importatante.\n    Desde corregir una falta ortográfica, agregar documentación, revisiones, etc.\n  </p>\n  <p>\n    Hemos redactado una guía con el paso a paso para que puedas iniciar a colaborar,\n    la puedes leer <a href="/guias/colaborar">aquí</a>.\n    Si te quedas atascada/o en un paso no dudes en preguntar en nuestro\n    <a href="https://t.me/pythonecuador">canal de telegram</a>\n    o en algún otro de nuestros <a href="/comunidades">canales de comunicación</a>.\n  </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/ayuda.tmpl", "uri": "ayuda.tmpl", "source_encoding": "utf-8", "line_map": {"35": 3, "53": 5, "54": 20, "55": 20, "40": 43, "27": 0, "61": 55, "46": 5}}
__M_END_METADATA
"""
