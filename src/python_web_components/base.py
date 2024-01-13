import abc
from typing import List

from python_web_components.utils import State


class AbstractWebComponent(abc.ABC):
    _context_stack = []

    def __init__(
        self,
        content: str | None = None,
        children: List["AbstractWebComponent"] | None = None,
        state: State | None = None,
        class_: str | None = None,
        id_: str | None = None,
        self_closing_tag: bool = False,
        keywords: List[str] | None = None,
        **kwargs,
    ):
        self._content = content
        self._children = children if children is not None else []
        self._state = state
        self._class = class_
        self._id = id_
        self._kwargs = kwargs
        self._keywords = keywords if keywords is not None else []
        self._self_closing_tag = self_closing_tag

        if self.state:
            self.state.subscribe(self.update)
            self.update()

        context = AbstractWebComponent.current_context()
        if context:
            context.add_child(self)

    def __enter__(self):
        AbstractWebComponent._context_stack.append(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        AbstractWebComponent._context_stack.pop()

    def add_child(self, child: "AbstractWebComponent") -> None:
        self._children.append(child)

    @classmethod
    def current_context(cls):
        if cls._context_stack:
            return cls._context_stack[-1]
        else:
            return None

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
    def self_closing_tag(self) -> bool:
        return self._self_closing_tag

    @property
    def html_attributes(self) -> str:
        attributes = {
            "id": self.id_,
            "class": self.class_,
            **{
                "hx-" + key.removeprefix("hx_") if key.startswith("hx_") else key: value
                for key, value in self._kwargs.items()
            },
        }

        return (
            " ".join(f'{key}="{value}"' for key, value in attributes.items() if value)
            + " "
            + " ".join(keyword for keyword in self._keywords if keyword).strip()
        ).strip()

    def render(self, depth: int | None = 0) -> str:
        indent = "\n" if depth != 0 else ""
        indent += " " * depth * 2  # 2 spaces per depth level
        content = self._content or "".join(
            child.render(depth + 1) for child in self._children if child is not None
        )
        attributes = f" {self.html_attributes}" if self.html_attributes else ""

        if self.self_closing_tag:
            return f"{indent}<{self.html_tag}{attributes} />"
        return f"{indent}<{self.html_tag}{attributes}>{content}\n{indent}</{self.html_tag}>"
