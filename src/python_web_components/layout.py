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
    @property
    def html_tag(self):
        return "li"
