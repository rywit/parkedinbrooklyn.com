from jinja2 import Environment, FileSystemLoader
import json


def get_env():
    return Environment(loader=FileSystemLoader("../templates"), trim_blocks=True)


def get_template():
    j2_env = get_env()
    return j2_env.get_template("state.html")


def get_content():
    with open("../config/content.json") as f:
        return json.load(f)


def build_rows(state):
    rows = []
    cur_row = []

    short_name = state["short_name"]
    pics = state["photos"]

    for pic in pics:
        cur_row.append({"short_name": short_name, "file_name": pic})

        if len(cur_row) == 3:
            rows.append(cur_row.copy())
            cur_row = []

    if len(cur_row) > 0:
        rows.append(cur_row.copy())

    return rows


def print_states_html():

    content = get_content()

    # Get template file
    template = get_template()

    for state in content["states"]:

        rows = build_rows(state)

        html = template.render(
            title="Parked In Brooklyn",
            rows=rows
        )

        # Where to save this rendered HTML
        file_name = "../html/states/%s.html" % state["short_name"]

        # Write HTML to disk
        file = open(file_name, "w")
        file.write(html)
        file.close()

        print("Wrote %s index file" % file_name)


if __name__ == '__main__':
    print_states_html()
