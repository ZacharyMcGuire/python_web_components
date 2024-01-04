from python_web_components.base import AbstractWebComponent


class P(AbstractWebComponent):
    @property
    def html_tag(self):
        return "p"


class H1(AbstractWebComponent):
    @property
    def html_tag(self):
        return "h1"


class H2(AbstractWebComponent):
    @property
    def html_tag(self):
        return "h2"
