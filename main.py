from fastapi import FastAPI
from routes.analysis.social import router as social_router
from routes.analysis.tech import router as tech_router
from routes.analysis.lexi import router as lexi_router

app = FastAPI()

app.include_router(social_router)
app.include_router(tech_router)
app.include_router(lexi_router)