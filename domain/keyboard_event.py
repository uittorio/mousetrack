from typing import TypedDict, Literal, Union


class KeyboardEvent(TypedDict):
    type: Union[Literal["click"], Literal["scroll"], Literal["move"]]
    time: str
