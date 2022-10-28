from typing import TypedDict, Literal, Union


class KeyboardEvent(TypedDict):
    type: Union[Literal["press"], Literal["release"]]
    time: str
