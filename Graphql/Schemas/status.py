import strawberry


@strawberry.type
class Status:
	success: bool
	message: str
