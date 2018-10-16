import python.renderer as rd


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
    template = rd.get_template("../templates/", "other.html")

    rows = build_plate_rows(photos)

    html = template.render(
        title="Parked In Brooklyn",
        rows=rows
    )

    # Write HTML to disk
    rd.write_html(html, "../html/other/index.html")


if __name__ == '__main__':

    content = rd.get_content("../config/content.json")
    print_other_landing_page(content["other"])
