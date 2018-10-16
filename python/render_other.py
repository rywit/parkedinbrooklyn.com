from jinja2 import Environment, FileSystemLoader
import json


def get_env():
    return Environment(loader=FileSystemLoader("../templates"), trim_blocks=True)


def get_template(template_name):
    j2_env = get_env()
    return j2_env.get_template(template_name)


def get_content():
    with open("../config/content.json") as f:
        return json.load(f)


def write_html(html, file_name):

    full_file_name = "../html/%s/index.html" % file_name

    file = open(full_file_name, "w")
    file.write(html)
    file.close()

    print("Wrote file: %s" % full_file_name)


def build_plate_rows(pics):
    rows = []
    cur_row = []

    for pic in pics:
        cur_row.append({"file_name": pic})

        if len(cur_row) == 3:
            rows.append(cur_row.copy())
            cur_row = []

    if len(cur_row) > 0:
        rows.append(cur_row.copy())

    return rows


def print_other_landing_page(photos):

    # Get template file
    template = get_template("other.html")

    rows = build_plate_rows(photos)

    html = template.render(
        title="Parked In Brooklyn",
        rows=rows
    )

    # Write HTML to disk
    write_html(html, "other")


if __name__ == '__main__':

    content = get_content()
    print_other_landing_page(content["other"])
