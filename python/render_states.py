from jinja2 import Environment, FileSystemLoader
import json


def get_env():
    return Environment(loader=FileSystemLoader("../templates"), trim_blocks=True)


def get_content():
    with open("../config/content.json") as f:
        return json.load(f)


def build_rows(content):
    rows = []
    cur_row = []

    for i in range(len(content)):
        cur_row.append(content[i])

        if len(cur_row) == 3:
            rows.append(cur_row.copy())
            cur_row = []

    if len(cur_row) > 0:
        rows.append(cur_row.copy())

    return rows


def print_states_html():

    content = get_content()
    rows = build_rows(content["states"])

    # Get our jinja environment
    j2_env = get_env()

    html = j2_env.get_template("states.html").render(
        title="Parked In Brooklyn",
        rows=rows
    )

    file = open("../html/states/index.html", "w")
    file.write(html)
    file.close()

    print("Wrote states index file")


if __name__ == '__main__':
    print_states_html()
