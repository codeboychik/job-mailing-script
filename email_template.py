from mako.template import Template


def get_filled_template(path, data):
    template = Template(filename=path)
    return template.render(data=data)

