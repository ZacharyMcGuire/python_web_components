from python_web_components.base import AbstractWebComponent
from python_web_components.utils import State


class Head(AbstractWebComponent):
    @property
    def html_tag(self):
        return "head"


class Body(AbstractWebComponent):
    @property
    def html_tag(self):
        return "body"


class Title(AbstractWebComponent):
    def __init__(self, content: str, **kwargs):
        self._content = content
        super().__init__(**kwargs)

    @property
    def html_tag(self):
        return "title"


class Html(AbstractWebComponent):
    def __init__(
        self,
        head: Head | None = None,
        body: Body | None = None,
        state: State | None = None,
        **kwargs,
    ):
        super().__init__(children=[head, body], state=state, **kwargs)

    @property
    def html_tag(self):
        return "html"

    def render(self, **kwargs):
        return "<!DOCTYPE html>" + super().render(**kwargs)


class Script(AbstractWebComponent):
    def __init__(self, src: str, **kwargs):
        super().__init__(src=src, **kwargs)

    @property
    def html_tag(self):
        return "script"


class Link(AbstractWebComponent):
    def __init__(self, href: str, **kwargs):
        super().__init__(href=href, self_closing_tag=True, **kwargs)

    @property
    def html_tag(self):
        return "link"
