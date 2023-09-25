import strawberry
from App.Services.note import NoteService
from App.Graphql.Schemas import NoteType
from App.Middleware.JWTBearer import IsAuthenticated


@strawberry.type
class Query:

	@strawberry.field(permission_classes=[IsAuthenticated])
	async def getAllNotes(self) -> list[NoteType]:
		return await NoteService.get_all_notes()

	@strawberry.field(permission_classes=[IsAuthenticated])
	async def getNote(self, id: int) -> NoteType:
		return await NoteService.get_by_id(id)
