from schema import NoteInput, NoteType
from Models.note import Note
from Repositories.note import NoteRepository
class NoteService:
   
   @staticmethod
   async def add_note(note_data: NoteInput):
      note = Note()
      note.name = note_data.name
      note.description = note_data.description
      await NoteRepository.create(note)

      return NoteType(id=note.id, name=note.name, description=note.description)
   
   @staticmethod
   async def get_by_id(id: int):
      note = await NoteRepository.get_by_id(id)
      return NoteType(id=note.id, name=note.name, description=note.description)
   
   @staticmethod
   async def get_all_notes():
      notes = await NoteRepository.get_all()
      return [NoteType(id=note.id, name=note.name, description=note.description) for note in notes]
   
   @staticmethod
   async def update(id: int, note_data: NoteInput):
      note = Note()
      note.name = note_data.name
      note.description = note_data.description
      await NoteRepository.update(id, note)
      return f'Note with id {id} updated successfully'
   
   @staticmethod
   async def delete(id: int):
      await NoteRepository.delete(id)
      return f'Note with id {id} deleted successfully'