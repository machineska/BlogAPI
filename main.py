import uvicorn
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
def index(limit: int = 50, published: bool = True, sort: Optional[str] = None):
    """Home Page Website"""
    if published:
        return {'data': f'{limit} published data blog list'}
    else:
        return {'data': f'{limit} data blog list'}


@app.get('/blog/unpublished')
def comments():
    """Fetch comments of blog with id = id"""
    return {'data': 'unpublished blog'}


@app.get('/blog/{id}')
def show(id: int):
    """Fetch blog with id"""
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    """Fetch comments of blog with id = id"""
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.get("/about")
def about():
    return {'data': 'about'}


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title is {blog.title}'}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

