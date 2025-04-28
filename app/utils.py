from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone
from jose import JWTError, jwt


pwd_content = CryptContext(schemes=["bcrypt"], deprecated = "auto")


ALGORITHM = "HS256"
SECRET_KEY = "asrorasinum"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 1800

def hash_password(password:str):
    return pwd_content.hash(password)

def verify_password(plain_password, hashed_password):
    print(">>>", hash_password(plain_password), hashed_password)
    return pwd_content.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: float = None):
    """
    Creates a new JWT token for logging-in user
    :param data:
    :param expires_delta:
    :return:
    """
    # Access tokenni nima bilan generatsiya qilaman?
    # Access token qanaqa token ozi?
    delta = timedelta(minutes=expires_delta) if expires_delta else timedelta(days = ACCESS_TOKEN_EXPIRE_MINUTES)
    expire_time = datetime.now(timezone.utc) + delta
    data.update({"exp": expire_time})

    # data = {"username": <>, "password": <>, "role": <>, "exp": <>}

    access_token = jwt.encode(data, SECRET_KEY, ALGORITHM)
    return access_token































