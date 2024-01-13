from python_web_components.base import AbstractWebComponent


class Div(AbstractWebComponent):
    @property
    def html_tag(self):
        return "div"


class Section(AbstractWebComponent):
    @property
    def html_tag(self):
        return "section"


class Ul(AbstractWebComponent):
    @property
    def html_tag(self):
        return "ul"


class Li(AbstractWebComponent):
    def __init__(self, content_=None, **kwargs):
        super().__init__(**kwargs)
        self.content = content_

    @property
    def html_tag(self):
        return "li"

    def render(self, depth: int = 0):
        indent = " " * depth * 2
        return f"{indent}<{self.html_tag}>{self.content}</{self.html_tag}>"
