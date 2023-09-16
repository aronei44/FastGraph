from sqlmodel import Field, SQLModel
class Note(SQLModel, table=True):
   __tablename__ = "notes"
   id: int = Field(default=None, primary_key=True)
   name: str
   description: str

