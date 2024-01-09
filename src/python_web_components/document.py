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
    @property
    def html_tag(self):
        return "title"


class Html(AbstractWebComponent):
    def __init__(self, head: Head | None = None, body: Body | None = None, state: State | None = None):
        super().__init__(children=[head, body], state=state)

    @property
    def html_tag(self):
        return "html"

    def render(self):
        return "<!DOCTYPE html>" + super().render()


class Script(AbstractWebComponent):
    def __init__(self, src: str):
        self._src = src
        super().__init__()

    @property
    def html_tag(self):
        return "script"

    def render(self):
        return f'<{self.html_tag} src="{self._src}"></{self.html_tag}>'


class Link(AbstractWebComponent):
    def __init__(self, href: str, rel: str | None = None, type: str | None = None):
        self._href = href
        self._rel = rel
        self._type = type
        super().__init__()

    @property
    def html_tag(self):
        return "link"

    def render(self):
        return f'<{self.html_tag} rel="{self._rel}" href="{self._href}" type="{self._type}">'
