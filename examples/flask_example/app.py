from flask import Flask
import python_web_components as ui

app = Flask(__name__)

example_list_of_records = ["First Record", "Second Record", "Third Record"]


@app.route("/")
def index():
    with ui.Html() as html:
        with ui.Head():
            ui.Title("Flask Example"),
            ui.Link(
                href="https://cdn.jsdelivr.net/npm/daisyui@4.5.0/dist/full.min.css",
                rel="stylesheet",
                type="text/css",
            ),
        with ui.Body():
            with ui.Div(class_="container mx-auto"):
                ui.H1("Flask Example"),
                ui.Button(
                    "Get Example Records",
                    class_="btn btn-primary",
                    hx_get="/get_records",
                    hx_trigger="click",
                    hx_swap="innerHTML",
                    hx_target="#records",
                ),
                ui.H1("Records"),
                with ui.Div(id_="records"):
                    ui.P("Click the button to get records...")
            ui.Script(src="https://unpkg.com/htmx.org"),
            ui.Script(src="https://cdn.tailwindcss.com"),

        return html.render()


@app.route("/get_records", methods=["GET"])
def get_records():
    with ui.Ul() as html:
        for record in example_list_of_records:
            ui.Li(record)

        return html.render()
