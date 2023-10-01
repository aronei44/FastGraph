import strawberry
import asyncio
from typing import AsyncGenerator
from App.Graphql.Schemas import Subs, Status

@strawberry.type
class Subscription:

	@strawberry.subscription
	async def count(self, target: int = 100) -> AsyncGenerator[Subs, None]:
		for i in range(target):
			data = Subs(
				stat=Status(success=i%2 ==0, message="Success" if i%2 ==0 else "Failed"),
				count=i
			)
			yield data
			await asyncio.sleep(1)
