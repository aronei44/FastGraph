from App.Graphql.Schemas import NoteInput, NoteType, Status
from App.Models import NoteModel
from App.Repositories import NoteRepository
from App.Helper import debugger


class NoteService:

	@staticmethod
	@debugger
	async def add_note(note_data: NoteInput):
		note = NoteModel()
		note.name = note_data.name
		note.description = note_data.description
		await NoteRepository.create(note)

		return NoteType(id=note.id, name=note.name, description=note.description)

	@staticmethod
	@debugger
	async def get_by_id(id: int):
		note = await NoteRepository.get_by_id(id)
		if not note:
			return None
		return NoteType(id=note.id, name=note.name, description=note.description)

	@staticmethod
	@debugger
	async def get_all_notes():
		notes = await NoteRepository.get_all()
		return [NoteType(id=note.id, name=note.name, description=note.description) for note in notes]

	@staticmethod
	@debugger
	async def update(id: int, note_data: NoteInput):
		note = NoteModel()
		note.name = note_data.name
		note.description = note_data.description
		res = await NoteRepository.update(id, note)
		return Status(success=res[0], message=res[1])

	@staticmethod
	@debugger
	async def delete(id: int):
		res = await NoteRepository.delete(id)
		return Status(success=res[0], message=res[1])
