from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

router = APIRouter(
    prefix="/protected",
    # This is the be executed every time for auth with supabase.
    dependencies=[Depends(lambda credentials=HTTPBearer(): get_current_user(credentials))]
)

# Replace with the Supabase JWT secret key from your Supabase project settings.
SUPABASE_JWT_SECRET = "YOUR_SUPABASE_JWT_SECRET"
ALGORITHM = "HS256"

def get_current_user(credentials: HTTPAuthorizationCredentials):
    token = credentials.credentials
    try:
        decoded_token = jwt.decode(token, SUPABASE_JWT_SECRET, algorithms=[ALGORITHM])
        return decoded_token
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )

# My example of a route here that will have already run get_current_user to show the data is protected
@router.get("/data", tags=["protected"])
def read_protected_data():
    return {"data": "This is protected data"}
