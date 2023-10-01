from App.Models import NoteModel 
from App.Config.Database import db
from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete
from App.Helper import debugger


class NoteRepository:

	@staticmethod
	@debugger
	async def create(note_data: NoteModel):
		async with db.SessionLocal() as session:
			async with session.begin():
				session.add(note_data)

			await db.commit_roll_back()

	@staticmethod
	@debugger
	async def get_by_id(id: int):
		async with db as session:
			stmt = select(NoteModel).where(NoteModel.id == id)
			result = await session.execute(stmt)
			note = result.scalars().first()
			return note

	@staticmethod
	@debugger
	async def get_all():
		async with db as session:
			stmt = select(NoteModel)
			result = await session.execute(stmt)
			notes = result.scalars().all()
			return notes

	@staticmethod
	@debugger
	async def update(id: int, note_data: NoteModel) -> [bool, str]:
		async with db as session:
			stmt = select(NoteModel).where(NoteModel.id == id)
			result = await session.execute(stmt)
			note = result.scalars().first()
			if not note:
				return [False, f'Note with id {id} not found']
			note.name = note_data.name
			note.description = note_data.description
			query = sql_update(NoteModel).where(NoteModel.id == id).values(**note.dict()).execution_options(synchronize_session="fetch")
			res = await session.execute(query)
			if not res:
				return [False, f'Note with id {id} not updated']
			await db.commit_roll_back()
			return [True, f'Note with id {id} updated successfully']

	@staticmethod
	@debugger
	async def delete(id: int):
		async with db as session:
			stmt = select(NoteModel).where(NoteModel.id == id)
			result = await session.execute(stmt)
			note = result.scalars().first()
			if not note:
				return [False, f'Note with id {id} not found']
			query = sql_delete(NoteModel).where(NoteModel.id == id)
			res = await session.execute(query)
			if not res:
				return [False, f'Note with id {id} not deleted']
			await db.commit_roll_back()
			return [True, f'Note with id {id} deleted successfully']
