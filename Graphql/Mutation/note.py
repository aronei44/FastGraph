import strawberry

from Services.note import NoteService
from Graphql.Schemas import NoteInput, NoteType, Status


@strawberry.type
class Mutation:

	@strawberry.mutation
	async def createNote(self, note: NoteInput) -> NoteType:
		return await NoteService.add_note(note)

	@strawberry.mutation
	async def updateNote(self, id: int, note: NoteInput) -> Status:
		return await NoteService.update(id, note)

	@strawberry.mutation
	async def deleteNote(self, id: int) -> Status:
		return await NoteService.delete(id)
