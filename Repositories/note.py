from Models import NoteModel 
from Config.Database import db
from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete
class NoteRepository:


   @staticmethod
   async def create(note_data: NoteModel):
      async with db.SessionLocal() as session:
         async with session.begin():
            session.add(note_data)

         await db.commit_roll_back()


   @staticmethod
   async def get_by_id(id: int):
      async with db as session:
         stmt = select(NoteModel).where(NoteModel.id == id)
         result = await session.execute(stmt)
         note = result.scalars().first()
         return note
         

   @staticmethod
   async def get_all():
      async with db as session:
         stmt = select(NoteModel)
         result = await session.execute(stmt)
         notes = result.scalars().all()
         return notes
   
   @staticmethod
   async def update(id: int, note_data: NoteModel):
      async with db as session:
         stmt = select(NoteModel).where(NoteModel.id == id)
         result = await session.execute(stmt)
         note = result.scalars().first()
         note.name = note_data.name
         note.description = note_data.description
         query = sql_update(NoteModel).where(NoteModel.id == id).values(**note.dict()).execution_options(synchronize_session="fetch")
         await session.execute(query)
         await db.commit_roll_back()

   @staticmethod
   async def delete(id: int):
      async with db as session:
         query = sql_delete(NoteModel).where(NoteModel.id == id)
         await session.execute(query)
         await db.commit_roll_back()