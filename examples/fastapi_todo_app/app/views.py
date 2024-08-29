from .schemas import Task

import python_web_components as ui


def index(tasks: [Task]) -> str:
    with ui.Html() as html:
        with ui.Head():
            ui.Title("Fast API Example")
            (
                ui.Link(
                    href="https://cdn.jsdelivr.net/npm/daisyui@4.5.0/dist/full.min.css",
                    rel="stylesheet",
                    type="text/css",
                ),
            )

        with ui.Body():
            with ui.Div(class_="container mx-auto px-4"):
                ui.H1("Fast API Example", class_="text-2xl")

                with ui.Div(id="records"):
                    with ui.Div(class_="columns-2"):
                        ui.H2("Tasks", class_="text-xl")
                        ui.Button(
                            "Create Sample Records",
                            id="create_sample_records",
                            hx_post="/api/tasks/sample",
                            hx_swap="none",
                            class_="btn btn-primary btn-sm float-end",
                        )

                    with ui.Div():
                        for task in tasks:
                            with ui.Li():
                                ui.A(
                                    content=task.summary,
                                    href=f"/task/{task.id}",
                                    hx_boost="true",
                                    hx_target="#records",
                                )

            ui.Script(src="https://unpkg.com/htmx.org")
            ui.Script(src="https://cdn.tailwindcss.com")

        return html.render()


def task_details(task: Task) -> str:
    summary = ui.H2(task.summary, class_="text-xl w-2/3")
    description = ui.P(content=task.description, class_="mt-4 px-2 text-lg bg-base-200")

    return ui.Div(
        children=[
            ui.Div(
                class_="mt-4",
                children=[
                    ui.Button(
                        content="&larr; Tasks",
                        class_="btn btn-sm",
                        hx_get="/",
                        hx_target="body",
                    ),
                ],
            ),
            ui.Div(
                class_="columns-2 mt-4",
                children=[
                    summary,
                    ui.Button(
                        "Delete", class_="btn btn-warning btn-sm w-1/3 float-end"
                    ),
                ],
            ),
            description,
        ]
    ).render()
