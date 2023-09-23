import typing

from strawberry.permission import BasePermission
from strawberry.types import Info
from .JWTManager import JWTManager


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request = info.context["request"]
        authentication = request.headers.get("authorization", None)
        if authentication:
            try:
                token = authentication.split("Bearer ")[-1]
                return JWTManager().verify_jwt(token)
            except Exception as e:
                print(e)
                return False

        return False