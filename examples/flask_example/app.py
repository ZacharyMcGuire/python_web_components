from flask import Flask
from python_web_components import (
    HtmlDocument,
    Script,
    Button,
    Body,
    Head,
    Title,
    H1,
    Ul,
    Li,
    Link,
    Div,
)

app = Flask(__name__)

example_list_of_records = ["First Record", "Second Record", "Third Record"]


class App(HtmlDocument):
    ...


@app.route("/")
def index():
    return App(
        Head(
            children=[
                Title("Flask Example"),
                Link(
                    href="https://cdn.jsdelivr.net/npm/daisyui@4.5.0/dist/full.min.css",
                    rel="stylesheet",
                    type="text/css",
                ),
            ],
        ),
        Body(
            children=[
                Div(
                    class_="container mx-auto",
                    children=[
                        H1(content="Flask Example"),
                        Button(
                            content="Get Example Records",
                            class_="btn btn-primary",
                            hx_get="/get_records",
                            hx_trigger="click",
                            hx_swap="outerHTML",
                        ),
                    ],
                ),
                Script(src="https://unpkg.com/htmx.org"),
                Script(src="https://cdn.tailwindcss.com"),
            ]
        ),
    ).render()


@app.route("/get_records", methods=["GET"])
def get_records():
    return Ul(
        children=[Li(content=record) for record in example_list_of_records]
    ).render()
