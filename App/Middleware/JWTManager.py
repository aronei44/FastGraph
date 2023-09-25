import os
from datetime import datetime, timedelta
from jose import jwt
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES"))


class JWTManager:


    @staticmethod
    def generate_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    

    @staticmethod
    def verify_jwt(token: str):
        try:
            decode_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            current_timestamp = datetime.utcnow().timestamp()
            if not decode_token:
                raise ValueError("Token is invalid")
            elif decode_token["exp"] < current_timestamp:
                raise ValueError("Token is expired")
            return True
        except ValueError as e:
            print(e)
            return False
            