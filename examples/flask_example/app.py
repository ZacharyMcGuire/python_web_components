from flask import Flask
import python_web_components as ui

app = Flask(__name__)

example_list_of_records = ["First Record", "Second Record", "Third Record"]


@app.route("/")
def index():
    with ui.Html() as html:
        with ui.Head():
            ui.Title("Flask Example")
            (
                ui.Link(
                    href="https://cdn.jsdelivr.net/npm/daisyui@4.5.0/dist/full.min.css",
                    rel="stylesheet",
                    type="text/css",
                ),
            )

        with ui.Body():
            with ui.Div(class_="container mx-auto"):
                ui.H1("Flask Example")
                (
                    ui.Button(
                        "Get Example Records",
                        class_="btn btn-primary",
                        hx_get="/get_records",
                        hx_trigger="click",
                        hx_swap="innerHTML",
                        hx_target="#records",
                    ),
                )

                ui.H1("Records")
                with ui.Div(id_="records"):
                    ui.P("Click the button to get records...")

                with ui.tag("p"):
                    ui.tag("a", content_="Python Web Components", href="#")

            ui.Script(src="https://unpkg.com/htmx.org")
            ui.Script(src="https://cdn.tailwindcss.com")

        return html.render()


@app.route("/get_records", methods=["GET"])
def get_records():
    with ui.Ul() as html:
        for record in example_list_of_records:
            ui.Li(record)

        return html.render()


@app.route("/shoelace-component-example")
def shoelace_component_example():
    with ui.Html() as html:
        with ui.Head():
            ui.Title("Shoelace Component Example")
            ui.Link(
                href="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.12.0/cdn/themes/light.css",
                rel="stylesheet",
                type="text/css",
            )
            ui.Script(
                type="module",
                src="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.12.0/cdn/shoelace-autoloader.js",
            )

        with ui.Body():
            with ui.tag("sl-card", class_="card-overview"):
                ui.Img(
                    slot="image",
                    src="https://images.unsplash.com/photo-1559209172-0ff8f6d49ff7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=80",
                    alt="A kitten sits patiently between a terracotta pot and decorative grasses.",
                )

                ui.tag("strong", content_="Mittens")
                ui.tag("br", self_closing_tag=True)

                ui.P("This kitten is as cute as he is playful. Bring him home today!")
                ui.tag("br", self_closing_tag=True)

                ui.tag("small", content_="6 weeks old")

                with ui.Div(slot="footer"):
                    ui.tag(
                        "sl-button",
                        variant="primary",
                        keywords=["pill"],
                        content_="More Info",
                    )
                    ui.tag("sl-rating")

            ui.tag(
                "style",
                content_="""
                .card-overview {
                    max-width: 300px;
                }

                .card-overview small {
                    color: var(--sl-color-neutral-500);
                }

                .card-overview [slot='footer'] {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }
                """,
            )

        return html.render()
