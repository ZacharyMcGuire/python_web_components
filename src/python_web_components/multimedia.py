from python_web_components.base import AbstractWebComponent


class Img(AbstractWebComponent):
    @property
    def html_tag(self):
        return "img"


class Video(AbstractWebComponent):
    @property
    def html_tag(self):
        return "video"
