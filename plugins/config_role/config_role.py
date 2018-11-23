from docutils.frontend import OptionParser
from docutils.parsers.rst import Parser, roles
from docutils.utils import new_document
from nikola.plugin_categories import RestExtension


class Plugin(RestExtension):

    name = 'config_role'

    def set_site(self, site):
        roles.register_canonical_role('config', config_role(site))
        return super().set_site(site)


def config_role(site):
    """
    Inject a value from the ``conf.py`` file.

    Before injecting the value, it is parsed by the rst parser,
    that way we can have a link when reading an email from the config
    for example.

    This role needs access to the `site` object.
    As we can't pass extra args to a role function we are using a closure.
    """
    def role(name, rawtext, text, lineno, inliner, options=None, content=None):
        parser = Parser()
        settings = OptionParser(components=(Parser,)).get_default_values()
        document = new_document('Raw rst from config value', settings)

        config_value = site.config.get(text, '')
        parser.parse(config_value, document)

        # The whole text is interpreted as a big paragraph
        # causing a new line to be inserted at the end,
        # so we only take the elements inside that paragraph.
        paragraph, *_ = document.children
        return paragraph.children, []
    return role
