from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status

from blog import database, models
from blog.routers import user
from .. import schemas, token
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/login')

def login(request: schemas.Login,db: Session = Depends(database.get_db)):
  
  user = db.query(models.User).filter(models.User.email == request.username).first()
  if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                          detail=f'User with the email {request.username} is not available')
  
  access_token = token.create_access_token(
     data={"sub": user.email}
  )
  return {"access_token": access_token, "token_type": "bearer"}