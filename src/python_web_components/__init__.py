from .base import AbstractWebComponent
from .document import Head, Body, Title, Html, Script, Link
from .text import P, H1, H2
from .multimedia import Img, Video
from .form import Input, Button
from .layout import Div, Section, Ul, Li
from .navigation import A, Nav

__all__ = [
    "Head",
    "Body",
    "Title",
    "Html",
    "Script",
    "P",
    "H1",
    "H2",
    "Img",
    "Video",
    "Input",
    "Button",
    "Div",
    "Ul",
    "Li",
    "Section",
    "A",
    "Nav",
    "Link",
]

known_tags = {
    "head": Head,
    "body": Body,
    "title": Title,
    "html": Html,
    "script": Script,
    "p": P,
    "h1": H1,
    "h2": H2,
    "img": Img,
    "video": Video,
    "input": Input,
    "button": Button,
    "div": Div,
    "ul": Ul,
    "li": Li,
    "section": Section,
    "a": A,
    "nav": Nav,
    "link": Link,
}


def tag(html_tag: str, **kwargs):
    """Generic html tag constructor.
    Generate a component from a tag name and keyword arguments.

    Args:
        tag (str): The tag name of the component.
        **kwargs: Keyword arguments to pass to the component.

    Returns:
        AbstractWebComponent: The generated component.
    """
    try:
        return known_tags[html_tag.lower()](**kwargs)
    except KeyError:

        class _(AbstractWebComponent):
            @property
            def html_tag(self):
                return html_tag

        return _(**kwargs)
