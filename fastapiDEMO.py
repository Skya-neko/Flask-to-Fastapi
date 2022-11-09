from fastapi import FastAPI
from typing import Optional
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Content-Type"],
)
@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    # Attention: Put static routing before dynamic routing.
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data': {'1', '2', '3'}}


if __name__ == '__main__':
    config = uvicorn.Config(app="fastapiDEMO:app",
                            host="0.0.0.0",
                            port=8080,
                            workers=4,
                            reload=True,
                            # thread = 2,
                            # master = true,
                            # chmod-socket = 660
                            # vacuum = true
                            # die-on-term = true
                            )


    server = uvicorn.Server(config)
    server.run()
