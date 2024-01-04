from python_web_components.base import AbstractWebComponent


class Input(AbstractWebComponent):
    @property
    def html_tag(self):
        return "input"


class Button(AbstractWebComponent):
    @property
    def html_tag(self):
        return "button"
