from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from sqlalchemy import select

from app.schemas.user_schema import UserCreate
from app.db.dependencies import get_db
from app.core.security import hash_password
from app.schemas.login_schema import LoginRequest
from app.core.security import verify_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/test")
def test_auth():
    return {"message": "Auth API Working"}


@router.post("/register")
async def register(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    
    result = await db.execute(
        select(User).where(User.email == user.email)
    )

    existing_user = result.scalar_one_or_none()

    if existing_user:
        return {"message": "Email already exists"}

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password),
        role="engineer"
    )

    db.add(new_user)

    await db.commit()

    await db.refresh(new_user)

    return {
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
        "message": "User registered successfully"
    }
    
@router.post("/login")
async def login(
    user: LoginRequest,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(User).where(User.email == user.email)
    )

    db_user = result.scalar_one_or_none()

    if not db_user:
        return {"message": "Invalid email or password"}

    if not verify_password(
        user.password,
        db_user.password_hash
    ):
        return {"message": "Invalid email or password"}

    return {
        "message": "Login successful",
        "user_id": db_user.id,
        "username": db_user.username
    }