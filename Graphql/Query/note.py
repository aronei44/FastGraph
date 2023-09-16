import strawberry
from Services.note import NoteService
from Graphql.Schemas import NoteType

@strawberry.type
class Query:

   @strawberry.field
   async def getAllNotes(self) -> list[NoteType]:
      return await NoteService.get_all_notes()
   
   @strawberry.field
   async def getNote(self, id: int) -> NoteType | None:
      return await NoteService.get_by_id(id)