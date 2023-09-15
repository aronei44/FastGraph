import strawberry

from service.note import NoteService
from schema import NoteInput, NoteType

@strawberry.type
class Mutation:

   @strawberry.mutation
   async def create(self, note: NoteInput) -> NoteType:
      return await NoteService.add_note(note)

   @strawberry.mutation
   async def update(self, id: int, note: NoteInput) -> str:
      return await NoteService.update(id, note)

   @strawberry.mutation
   async def delete(self, id: int) -> str:
      return await NoteService.delete(id)