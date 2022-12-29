from fastapi import FastAPI
from dotenv import load_dotenv
from routes.auth import auth_routes
from routes.routes import route
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
app.include_router(auth_routes, prefix="/api")
app.include_router(route, prefix="/api")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

