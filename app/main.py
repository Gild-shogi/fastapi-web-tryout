from fastapi import FastAPI, Form, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("main.jinja2", {"request": request})

@app.get("/search/", response_class=HTMLResponse)
def search(request:Request, query:str=Query(default="")):
    return templates.TemplateResponse("search.jinja2", {"request":request, "query": query})

@app.post("/item/", response_class=HTMLResponse)
def item(request:Request, item:str = Form()):
    return templates.TemplateResponse("item.jinja2", {"request":request, "item": item})
