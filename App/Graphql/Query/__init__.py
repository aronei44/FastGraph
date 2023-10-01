import strawberry
from .note import Query as NoteQuery


@strawberry.type
class Query(NoteQuery):
    pass
