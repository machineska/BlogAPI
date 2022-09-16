from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {'data': 'blog list'}


@app.get('/blog/unpublished')
def comments():
    """Fetch comments of blog with id = id"""
    return {'data': 'unpublished blog'}


@app.get('/blog/{id}')
def show(id: int):
    """Fetch blog with id"""
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    """Fetch comments of blog with id = id"""
    return {'data': {'1', '2'}}


@app.get("/about")
def about():
    return {'data': 'about'}
