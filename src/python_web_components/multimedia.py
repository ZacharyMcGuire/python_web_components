from python_web_components.base import AbstractWebComponent


class Img(AbstractWebComponent):
    def __init__(self, self_closing_tag: bool = True, **kwargs):
        super().__init__(self_closing_tag=self_closing_tag, **kwargs)

    @property
    def html_tag(self):
        return "img"


class Video(AbstractWebComponent):
    @property
    def html_tag(self):
        return "video"
