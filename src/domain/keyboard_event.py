from typing import TypedDict, Literal, Union


class KeyboardEvent(TypedDict):
    type: Union[Literal["keypressed"]]
    time: float
