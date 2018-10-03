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

    full_file_name = "../html/states/%s.html" % file_name

    file = open(full_file_name, "w")
    file.write(html)
    file.close()

    print("Wrote file: %s" % full_file_name)


def build_plate_rows(state):
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


def build_landing_rows(states):
    rows = []
    cur_row = []

    for i in range(len(states)):
        cur_row.append(states[i])

        if len(cur_row) == 3:
            rows.append(cur_row.copy())
            cur_row = []

    if len(cur_row) > 0:
        rows.append(cur_row.copy())

    return rows


def print_individual_state_pages(states):

    # Get template file
    template = get_template("state.html")

    for state in states:

        rows = build_plate_rows(state)

        html = template.render(
            title="Parked In Brooklyn",
            rows=rows
        )

        # Write HTML to disk
        write_html(html, state["short_name"])


def print_states_landing_page(states):

    # Get template file
    template = get_template("states.html")

    # Build rows of data
    rows = build_landing_rows(states)

    html = template.render(
        title="Parked In Brooklyn",
        rows=rows
    )

    write_html(html, "index")


if __name__ == '__main__':

    content = get_content()
    print_states_landing_page(content["states"])
    print_individual_state_pages(content["states"])
