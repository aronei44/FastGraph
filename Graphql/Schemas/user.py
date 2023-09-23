import strawberry

@strawberry.input
class RegisterInput:
    username: str
    password: str
    email: str


@strawberry.input
class LoginInput:
    email: str
    password: str


@strawberry.type
class LoginType:
    email: str
    token: str