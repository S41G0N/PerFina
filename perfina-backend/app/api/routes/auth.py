from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from services.auth import (
    authenticate_user,
    create_access_token,
    get_current_user,
    get_password_hash,
)
from schemas.user import Token, UserCreate, UserPydantic
from models.user import User
from datetime import timedelta

from config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expiry_time = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expiry_time
    )
    return {"access_token": access_token, "token_type": "bearer"}


# REGISTER USER IF USERNAME IS UNIQUE
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate):
    db_user = await User.get_or_none(username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = await User.create(
        username=user.username, hashed_password=get_password_hash(user.password)
    )
    return {"message": f"User created successfully: {user.username}"}


# PRINT CURRENT USER AFTER SUCCESSFUL LOGIN USING TOKEN
@router.get("/users/me", response_model=UserPydantic)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return await UserPydantic.from_tortoise_orm(current_user)


@router.get("/protected")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}"}
