from fastapi import FastAPI
from database import models
from database.database import engine
from routers import post
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Bring in router and all endpoints
app.include_router(post.router)

#create the database
models.Base.metadata.create_all(bind=engine)

#make folder images accessible outside of project
app.mount('/images', StaticFiles(directory='images'), name='images')

origins = {
  'http://localhost:3000'
}

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)