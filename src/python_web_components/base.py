import abc
from typing import List

from python_web_components.utils import State


class AbstractWebComponent(abc.ABC):
    def __init__(
        self,
        content: str | None = None,
        children: List["AbstractWebComponent"] | None = None,
        state: State | None = None,
        class_: str | None = None,
        id_: str | None = None,
        **kwargs,
    ):
        self._content = content
        self._children = children
        self._state = state
        self._class = class_
        self._id = id_
        self._kwargs = kwargs

        if self.state:
            self.state.subscribe(self.update)
            self.update()

    @property
    def class_(self) -> str | None:
        return self._class

    @property
    def id_(self) -> str | None:
        return self._id

    @property
    def state(self) -> State | None:
        return self._state

    def update(self) -> None:
        if self.html_tag in self._state._state:  # Check if html_tag is in the state
            new_content = self._state[self.html_tag]
            if new_content != self._content:
                self.content = new_content

    @property
    def content(self) -> str | None:
        return self._content

    @content.setter
    def content(self, value) -> None:
        self._content = value
        if self._state:
            self._state.notify()

    def subscribe(self, observer) -> None:
        self._state.subscribe(observer)

    @abc.abstractproperty
    def html_tag(self):
        pass

    @property
    def html_attributes(self) -> str:
        attributes = {
            "id": self.id_,
            "class": self.class_,
            **self._kwargs,
        }

        # Fix HTMX kwarg names
        for key, value in list(attributes.items()):
            if key.startswith("hx_"):
                value = attributes.pop(key)
                new_key = "hx-" + key.removeprefix("hx_")
                attributes[new_key] = value

        return " ".join(
            f'{key}="{value}"' for key, value in attributes.items() if value
        )

    def render(self) -> str:
        content = self._content or "".join(child.render() for child in self._children)
        attributes = f" {self.html_attributes}" if self.html_attributes else ""
        return f"<{self.html_tag}{attributes}>{content}</{self.html_tag}>"