# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1526136318.166286
_enable_loop = True
_template_filename = '/home/ela/entornos/pyecEnv/lib/python3.5/site-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl'
_template_uri = 'feeds_translations_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['head', 'feed_link', 'translation_link']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,classification=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        other_languages = context.get('other_languages', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        if len(translations) > 1:
            for language in sorted(translations):
                if classification:
                    if generate_atom:
                        __M_writer('                    <link rel="alternate" type="application/atom+xml" title="Atom for ')
                        __M_writer(str(kind))
                        __M_writer(' ')
                        __M_writer(filters.html_escape(str(classification)))
                        __M_writer(' (')
                        __M_writer(str(language))
                        __M_writer(')" href="')
                        __M_writer(str(_link(kind + "_atom", classification, language)))
                        __M_writer('">\n')
                    if generate_rss and not rss_link:
                        __M_writer('                    <link rel="alternate" type="application/rss+xml" title="RSS for ')
                        __M_writer(str(kind))
                        __M_writer(' ')
                        __M_writer(filters.html_escape(str(classification)))
                        __M_writer(' (')
                        __M_writer(str(language))
                        __M_writer(')" href="')
                        __M_writer(str(_link(kind + "_rss", classification, language)))
                        __M_writer('">\n')
                else:
                    if generate_atom:
                        __M_writer('                    <link rel="alternate" type="application/atom+xml" title="Atom (')
                        __M_writer(str(language))
                        __M_writer(')" href="')
                        __M_writer(str(_link("index_atom", None, language)))
                        __M_writer('">\n')
                    if generate_rss and not rss_link:
                        __M_writer('                    <link rel="alternate" type="application/rss+xml" title="RSS (')
                        __M_writer(str(language))
                        __M_writer(')" href="')
                        __M_writer(str(_link("rss", None, language)))
                        __M_writer('">\n')
        else:
            if classification:
                if generate_atom:
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom for ')
                    __M_writer(str(kind))
                    __M_writer(' ')
                    __M_writer(filters.html_escape(str(classification)))
                    __M_writer('" href="')
                    __M_writer(str(_link(kind + "_atom", classification)))
                    __M_writer('">\n')
                if generate_rss and not rss_link:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS for ')
                    __M_writer(str(kind))
                    __M_writer(' ')
                    __M_writer(filters.html_escape(str(classification)))
                    __M_writer('" href="')
                    __M_writer(str(_link(kind + "_rss", classification)))
                    __M_writer('">\n')
            else:
                if generate_atom:
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                    __M_writer(str(_link("index_atom", None)))
                    __M_writer('">\n')
                if generate_rss and not rss_link:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                    __M_writer(str(_link("rss", None)))
                    __M_writer('">\n')
        if has_other_languages and other_languages:
            for language, classification, _ in other_languages:
                __M_writer('            <link rel="alternate" hreflang="')
                __M_writer(str(language))
                __M_writer('" href="')
                __M_writer(str(_link(kind, classification, language)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_feed_link(context,classification):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for language in sorted(translations):
                if generate_atom or generate_rss:
                    __M_writer('                <p class="feedlink">\n')
                    if generate_atom:
                        __M_writer('                        <a href="')
                        __M_writer(str(_link(kind + "_atom", classification, language)))
                        __M_writer('" hreflang="')
                        __M_writer(str(language))
                        __M_writer('" type="application/atom+xml">')
                        __M_writer(str(messages('Atom feed', language)))
                        __M_writer(' (')
                        __M_writer(str(language))
                        __M_writer(')</a>\n')
                    if generate_rss:
                        __M_writer('                        <a href="')
                        __M_writer(str(_link(kind + "_rss", classification, language)))
                        __M_writer('" hreflang="')
                        __M_writer(str(language))
                        __M_writer('" type="application/rss+xml">')
                        __M_writer(str(messages('RSS feed', language)))
                        __M_writer(' (')
                        __M_writer(str(language))
                        __M_writer(')</a>\n')
                    __M_writer('                </p>\n')
        else:
            if generate_atom or generate_rss:
                __M_writer('            <p class="feedlink">\n')
                if generate_atom:
                    __M_writer('                    <a href="')
                    __M_writer(str(_link(kind + "_atom", classification)))
                    __M_writer('" type="application/atom+xml">')
                    __M_writer(str(messages('Atom feed')))
                    __M_writer('</a>\n')
                if generate_rss:
                    __M_writer('                    <a href="')
                    __M_writer(str(_link(kind + "_rss", classification)))
                    __M_writer('" type="application/rss+xml">')
                    __M_writer(str(messages('RSS feed')))
                    __M_writer('</a>\n')
                __M_writer('            </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_translation_link(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        other_languages = context.get('other_languages', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if has_other_languages and other_languages:
            __M_writer('        <div class="translationslist translations">\n            <h3 class="translationslist-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h3>\n')
            for language, classification, name in other_languages:
                __M_writer('            <p><a href="')
                __M_writer(str(_link(kind, classification, language)))
                __M_writer('" rel="alternate">')
                __M_writer(str(messages("LANGUAGE", language)))
                __M_writer('\n')
                if kind != 'archive':
                    __M_writer('                (')
                    __M_writer(filters.html_escape(str(name)))
                    __M_writer(')\n')
                __M_writer('            </a></p>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/ela/entornos/pyecEnv/lib/python3.5/site-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl", "uri": "feeds_translations_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 48, "23": 76, "24": 91, "30": 4, "44": 4, "45": 5, "46": 6, "47": 6, "48": 6, "49": 8, "50": 9, "51": 10, "52": 11, "53": 12, "54": 12, "55": 12, "56": 12, "57": 12, "58": 12, "59": 12, "60": 12, "61": 12, "62": 14, "63": 15, "64": 15, "65": 15, "66": 15, "67": 15, "68": 15, "69": 15, "70": 15, "71": 15, "72": 17, "73": 18, "74": 19, "75": 19, "76": 19, "77": 19, "78": 19, "79": 21, "80": 22, "81": 22, "82": 22, "83": 22, "84": 22, "85": 26, "86": 27, "87": 28, "88": 29, "89": 29, "90": 29, "91": 29, "92": 29, "93": 29, "94": 29, "95": 31, "96": 32, "97": 32, "98": 32, "99": 32, "100": 32, "101": 32, "102": 32, "103": 34, "104": 35, "105": 36, "106": 36, "107": 36, "108": 38, "109": 39, "110": 39, "111": 39, "112": 43, "113": 44, "114": 45, "115": 45, "116": 45, "117": 45, "118": 45, "124": 50, "136": 50, "137": 51, "138": 52, "139": 53, "140": 54, "141": 55, "142": 56, "143": 56, "144": 56, "145": 56, "146": 56, "147": 56, "148": 56, "149": 56, "150": 56, "151": 58, "152": 59, "153": 59, "154": 59, "155": 59, "156": 59, "157": 59, "158": 59, "159": 59, "160": 59, "161": 61, "162": 64, "163": 65, "164": 66, "165": 67, "166": 68, "167": 68, "168": 68, "169": 68, "170": 68, "171": 70, "172": 71, "173": 71, "174": 71, "175": 71, "176": 71, "177": 73, "183": 78, "192": 78, "193": 79, "194": 80, "195": 81, "196": 81, "197": 82, "198": 83, "199": 83, "200": 83, "201": 83, "202": 83, "203": 84, "204": 85, "205": 85, "206": 85, "207": 87, "208": 89, "214": 208}}
__M_END_METADATA
"""
