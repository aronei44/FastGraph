import strawberry
from .note import Mutation as NoteMutation
from .user import Mutation as UserMutation

@strawberry.type
class Mutation(UserMutation, NoteMutation):
   	pass
