from fastapi import APIRouter, HTTPException, status
from app.schemas import LoginRequest, Token
from app.auth import authenticate_user, create_access_token

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/login", response_model=Token)
def login(request: LoginRequest):
    if not authenticate_user(request.username, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(data={"sub": request.username})
    return Token(access_token=access_token, token_type="bearer")
