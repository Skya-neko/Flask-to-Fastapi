from fastapi import FastAPI
from .routers import example
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
app.include_router(example.router)

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Content-Type"],
)

config = uvicorn.Config(
    app="app:app",
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

