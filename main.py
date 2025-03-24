from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.analysis.social import router as social_router
from routes.analysis.tech import router as tech_router
from routes.analysis.lexi import router as lexi_router

app = FastAPI()

allowed_origins = [
    "https://www.trade-x.me",
    "https://www.trade-x.me/",
    "https://trade-x.me",
    "https://trade-x.me/",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(social_router)
app.include_router(tech_router)
app.include_router(lexi_router)