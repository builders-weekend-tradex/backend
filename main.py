from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, Request
from typing import Union
from routes.analysis.social import router as social_router
from routes.analysis.tech import router as tech_router
from routes.analysis.lexi import router as lexi_router

app = FastAPI()

origins = [
    "https://www.trade-x.me",
    "https://www.trade-x.me/"
    "https://trade-x.me",
    "https://trade-x.me/",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def exception_handler(request: Request, exception: Union[Exception, RuntimeError]):
    headers = {
        'Access-Control-Allow-Origin': ', '.join(origins),
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Allow-Methods': '*',
        'Access-Control-Allow-Headers': '*',
    }
    if isinstance(exception, EntityException):
        response = JSONResponse(
            jsonable_encoder(
                {
                    "code": exception.code,
                    "message": exception.message,
                    "exception": exception.exception
                }
            ),
            headers=headers
        )
    else:
        response = JSONResponse(
            jsonable_encoder(
                {
                    "exception": str(exception),
                    "code": 500,
                }
            ),
            headers=headers
        )
    return response

app.include_router(social_router)
app.include_router(tech_router)
app.include_router(lexi_router)