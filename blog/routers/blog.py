from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, models, database
from sqlalchemy.orm import Session


router = APIRouter(
    tags=['Blogs']
    
)

@router.get('/blog', response_model=List[schemas.ShowBlog])

  #db: Session = Depends(get_db) used for getting the db session
def all(db: Session = Depends(database.get_db)):
    
   # db.query(models.Blog).all() used for calling all blogs from the db
    blogs = db.query(models.Blog).all()
    return blogs


@router.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(database.get_db)):
    blog =db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'
   
@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog =db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with the id {id} is not available')
    
    blog.update({"title": request.title, "body": request.body}, synchronize_session=False)
    db.commit()
    
    return 'updated'

@router.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)

def show(id,db: Session = Depends(database.get_db)):
    #filter(models.Blog.id == id).first() used for filtering the blog with the given id
    blog = db.query(models.Blog).filter(models.Blog.id == id).first() 
    
    if not blog:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'details': f'Blog with the id {id} is not available'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with the id {id} is not available')
    
    
        
    return blog