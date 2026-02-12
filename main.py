from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# app is an instance of FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {'data':{"name": "Uthman", "age": 25}}

@app.get("/blog/comments")
def comments():
    #fetch comments of
  return {'data': "comments of the blog"}

@app.get("/blog/{id}")
def about(id):
    #fetch blog with id =id
    return {'data': id}

class Blog(BaseModel):
  title:str 
  content:str 
  published: Optional[bool]

@app.post("/blog/create")
def create_blog(blog: Blog):
    return {"data": f"Blog is created with title as {blog.title}"}

#if __name__ == "__main__":
#    import uvicorn
 #   uvicorn.run(app, host='127.0.0' ,port=8000)


@app.get("/status")
def get_status():
    return {"status": "API is running smoothly"}

# Version B: Change from Branch One