from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.ecu_routes import router as ecu_router
from app.api.websocket import router as websocket_router

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(ecu_router)
app.include_router(websocket_router)


@app.get("/")
def home():
    return {
        "message": "Smart Gateway ECU Simulator Running 🚗⚡"
    }