import pkg_resources
from jinja2 import Template


def get_template():
    template = 'templates/preseed.cfg.jinja'
    preseed = pkg_resources.resource_string('netinstauto', template).decode()
    return Template(preseed)
