from Models import UserModel 
from Config.Database import db
from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete


class UserRepository:

	@staticmethod
	async def create(user_data: UserModel):
		async with db.SessionLocal() as session:
			async with session.begin():
				session.add(user_data)

			await db.commit_roll_back()

	@staticmethod
	async def get_by_id(id: int):
		async with db as session:
			stmt = select(UserModel).where(UserModel.id == id)
			result = await session.execute(stmt)
			user = result.scalars().first()
			return user

	@staticmethod
	async def get_all():
		async with db as session:
			stmt = select(UserModel)
			result = await session.execute(stmt)
			users = result.scalars().all()
			return users

	@staticmethod
	async def update(id: int, user_data: UserModel) -> [bool, str]:
		async with db as session:
			stmt = select(UserModel).where(UserModel.id == id)
			result = await session.execute(stmt)
			user = result.scalars().first()
			if not user:
				return [False, f'user with id {id} not found']
			user.name = user_data.name
			user.email = user_data.email
			query = sql_update(UserModel).where(UserModel.id == id).values(**user.dict()).execution_options(synchronize_session="fetch")
			res = await session.execute(query)
			if not res:
				return [False, f'user with id {id} not updated']
			await db.commit_roll_back()
			return [True, f'user with id {id} updated successfully']

	@staticmethod
	async def delete(id: int):
		async with db as session:
			stmt = select(UserModel).where(UserModel.id == id)
			result = await session.execute(stmt)
			user = result.scalars().first()
			if not user:
				return [False, f'user with id {id} not found']
			query = sql_delete(UserModel).where(UserModel.id == id)
			res = await session.execute(query)
			if not res:
				return [False, f'user with id {id} not deleted']
			await db.commit_roll_back()
			return [True, f'user with id {id} deleted successfully']


	@staticmethod
	async def get_by_email(email: str):
		async with db as session:
			stmt = select(UserModel).where(UserModel.email == email)
			result = await session.execute(stmt)
			user = result.scalars().first()
			return user