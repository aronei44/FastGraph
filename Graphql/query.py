import strawberry
from Services.note import NoteService
from schema import NoteInput, NoteType

@strawberry.type
class Query:

   @strawberry.field
   def hello(self) -> str:
      return "Hello, world!"
   
   @strawberry.field
   async def get_all(self) -> list[NoteType]:
      return await NoteService.get_all_notes()
   
   @strawberry.field
   async def get_by_id(self, id: int) -> NoteType:
      return await NoteService.get_by_id(id)