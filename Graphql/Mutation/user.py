import strawberry

from Services import AuthService
from Graphql.Schemas import RegisterInput, LoginInput, LoginType, Status


@strawberry.type
class Mutation:


	@strawberry.mutation
	async def register(self, register_input: RegisterInput) -> Status:
		return await AuthService.register(register_input)

	@strawberry.mutation
	async def login(self, login_input: LoginInput) -> LoginType:
		return await AuthService.login(login_input)

