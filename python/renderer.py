from jinja2 import Environment, FileSystemLoader
import json


def get_template(template_dir, template_name):
    j2_env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True)
    return j2_env.get_template(template_name)


def get_content(content):
    with open(content) as f:
        return json.load(f)


def write_html(html, full_path):

    file = open(full_path, "w")
    file.write(html)
    file.close()

    print("Wrote file: %s" % full_path)
