
import os
from fastapi import Header, HTTPException, status

SECRET_TOKEN = os.getenv("BACKEND_AUTH_TOKEN")

def verify_token(x_token: str = Header(...)):
    if not SECRET_TOKEN or x_token != SECRET_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Unauthorized: Invalid or missing X-Token"
        )
    return True