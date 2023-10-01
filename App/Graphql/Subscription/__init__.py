import strawberry
from .example import Subscription as ExampleSubscription


@strawberry.type
class Subscription(ExampleSubscription):
    pass
