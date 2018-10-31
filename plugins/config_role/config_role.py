from docutils import nodes
from docutils import utils
from docutils.parsers.rst import roles
from nikola.plugin_categories import RestExtension


class Plugin(RestExtension):

    name = 'config_role'

    def set_site(self, site):
        config_role.site = site
        roles.register_canonical_role('config', config_role)
        return super().set_site(site)


def config_role(
        name, rawtext, text, lineno, inliner, options=None, content=None):
    options = options or {}
    content = content or []
    #  print(config_role.site.GLOBAL_CONTEXT)
    config = config_role.site.config.get(text, '')
    return [nodes.inline(rawtext, config)], []
