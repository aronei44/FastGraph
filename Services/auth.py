from passlib.context import CryptContext

from Models import UserModel
from Repositories import UserRepository
from Graphql.Schemas import RegisterInput, LoginInput, LoginType, Status
from Middleware.JWTManager import JWTManager


class AuthService:

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    async def login(login_input: LoginInput):
        user = await UserRepository.get_by_email(login_input.email)
        if not user:
            raise Exception("Email or password is incorrect")
        elif not AuthService.pwd_context.verify(login_input.password, user.password):
            raise Exception("Email or password is incorrect")
        token = JWTManager.generate_token({"sub": user.email})
        return LoginType(token=token, email=user.email)

    @staticmethod
    async def register(register_input: RegisterInput):
        existing_user = await UserRepository.get_by_email(register_input.email)
        if existing_user:
            raise Exception("Email already registered")
        hashed_password = AuthService.pwd_context.hash(register_input.password)
        user = UserModel(name=register_input.username, email=register_input.email, password=hashed_password)
        await UserRepository.create(user)
        return Status(success=True, message="User created successfully")