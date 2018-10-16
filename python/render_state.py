import python.renderer as rd


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

        states[i]["num_photos"] = len(states[i]["photos"])
        cur_row.append(states[i])

        if len(cur_row) == 3:
            rows.append(cur_row.copy())
            cur_row = []

    if len(cur_row) > 0:
        rows.append(cur_row.copy())

    return rows


def print_individual_state_pages(states):

    # Get template file
    template = rd.get_template("../templates/", "state.html")

    for state in states:

        rows = build_plate_rows(state)

        html = template.render(
            title="Parked In Brooklyn",
            full_name=state["full_name"],
            href=state["href"],
            rows=rows
        )

        # Write HTML to disk
        full_name = "../html/states/%s.html" % state["short_name"]
        rd.write_html(html, full_name)


def print_states_landing_page(states):

    # Get template file
    template = rd.get_template("../templates/", "states.html")

    # Build rows of data
    rows = build_landing_rows(states)

    html = template.render(
        title="Parked In Brooklyn",
        rows=rows
    )

    rd.write_html(html, "../html/states/index.html")


if __name__ == '__main__':

    content = rd.get_content("../config/content.json")
    print_states_landing_page(content["states"])
    print_individual_state_pages(content["states"])
