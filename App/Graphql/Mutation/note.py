import strawberry

from App.Services.note import NoteService
from App.Graphql.Schemas import NoteInput, NoteType, Status
from App.Middleware.JWTBearer import IsAuthenticated

@strawberry.type
class Mutation:

	@strawberry.mutation(permission_classes=[IsAuthenticated])
	async def createNote(self, note: NoteInput) -> NoteType:
		return await NoteService.add_note(note)

	@strawberry.mutation(permission_classes=[IsAuthenticated])
	async def updateNote(self, id: int, note: NoteInput) -> Status:
		return await NoteService.update(id, note)

	@strawberry.mutation(permission_classes=[IsAuthenticated])
	async def deleteNote(self, id: int) -> Status:
		return await NoteService.delete(id)
