import strawberry
from .status import Status


@strawberry.type
class Subs:
    stat: Status
    count: int
