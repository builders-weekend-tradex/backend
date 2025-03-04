from fastapi import FastAPI
from routes import protected

app = FastAPI()

# This includes the protected routes for supabase
app.include_router(protected.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
