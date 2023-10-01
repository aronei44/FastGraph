import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
load_dotenv()

DB_HOST = os.getenv("DB_HOST") or "localhost"
DB_PORT = os.getenv("DB_PORT") or 5432
DB_USER = os.getenv("DB_USER") or "postgres"
DB_PASSWORD = os.getenv("DB_PASSWORD") or "postgres"
DB_NAME = os.getenv("DB_NAME") or "postgres"
DB = os.getenv("DB") or "postgre"

DB_CONFIG = f"sqlite+aiosqlite:///./{DB_NAME}.db"

match DB:
	case "postgre":
		DB_CONFIG = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
	case "mysql":
		DB_CONFIG = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
	case _:
		DB_CONFIG = f"sqlite+aiosqlite:///./{DB_NAME}.db"


class DatabaseSession:
	def __init__(self, url:str=DB_CONFIG) -> None:
		self.engine = create_async_engine(url, echo=True)
		self.SessionLocal = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)
		self.session = self.SessionLocal()

	async def create_all(self):
		async with self.engine.begin() as conn:
			await conn.run_sync(SQLModel.metadata.create_all) 

	async def drop_all(self):
		async with self.engine.begin() as conn:
			await conn.run_sync(SQLModel.metadata.drop_all) 

	async def close(self):
		await self.engine.dispose()

	async def __aenter__(self) -> AsyncSession:
		self.session = self.SessionLocal()
		return self.session

	async def __aexit__(self, exc_type, exc_val, exc_tb):
		await self.session.close()

	async def commit_roll_back(self):
		try:
			await self.session.commit()
		except Exception as e:
			await self.session.rollback()
			raise


db = DatabaseSession()