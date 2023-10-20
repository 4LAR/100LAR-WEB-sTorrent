from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi import *

from globals import *
from routers import *

app = FastAPI()

app.include_router(router, prefix="")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
