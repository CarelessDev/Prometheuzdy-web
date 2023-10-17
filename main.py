# Load dotenv file if exists
try:
    from dotenv import load_dotenv
    load_dotenv('secrets.env')
except:
    pass

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.rest.router import router as rest_router
from app.api.web.router import router as web_router



app = FastAPI()


# Mount the static files directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include the routers
app.include_router(rest_router, prefix="/api")
app.include_router(web_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)