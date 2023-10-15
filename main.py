from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.index import router as index_router
from app.api.routes.auth import router as auth_router
from app.api.routes.user import router as user_router
from app.api.routes.mc import router as mc_router

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(index_router, tags=["index"])
app.include_router(auth_router, tags=["auth"])
app.include_router(user_router, tags=["user"])
app.include_router(mc_router, tags=["mc"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)