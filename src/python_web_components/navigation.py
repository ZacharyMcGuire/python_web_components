from python_web_components.base import AbstractWebComponent


class A(AbstractWebComponent):
    @property
    def html_tag(self):
        return "a"


class Nav(AbstractWebComponent):
    @property
    def html_tag(self):
        return "nav"
