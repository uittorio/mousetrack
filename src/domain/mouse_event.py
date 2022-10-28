from typing import TypedDict, Literal, Union


class MouseEvent(TypedDict):
    type: Union[Literal["click"], Literal["scroll"], Literal["move"]]
    time: str
