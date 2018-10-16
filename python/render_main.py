import python.renderer as rd


def print_main_landing_page(photos):

    # Get template file
    template = rd.get_template("../templates/", "main.html")

    html = template.render(
        title="Parked In Brooklyn",
        elems=photos
    )

    # Write HTML to disk
    rd.write_html(html, "../html/index.html")


if __name__ == '__main__':

    content = rd.get_content("../config/content.json")
    print_main_landing_page(content["main"])
