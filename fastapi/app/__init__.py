import configparser
from fastapi import FastAPI
from .routers import example
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

config = configparser.ConfigParser()
config.read('app.ini')
appConfig = config['app']
uvicornConfig = config['uvicorn']


app = FastAPI()
app.include_router(example.router)
app.add_middleware(
    CORSMiddleware,
    **appConfig
)

asgiConfig = uvicorn.Config(
    port=8080,
    **uvicornConfig,
)

server = uvicorn.Server(asgiConfig)

