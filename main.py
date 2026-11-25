import logging
import fastapi, uvicorn
import string
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LinkService(BaseModel):
    id: int
    url: str
    visits: int

data = [
    LinkService(id=1, url="http:abc.com", visits=45),
    LinkService(id=2, url="http:xyz.com", visits=0)
]

@app.get("/links/short/{id}")
def ShortToOrg(id: int):
    for links in data:
        if links.id == id:
            links.visits += 1
            logging.info(f"visited {links.url} -> {links.visits}")
            return {"Original Link": links.url, "Visits": links.visits}
    
    return "Invalid ID number"

@app.post("/links/org/{url}")
def OrgToShort(url: str):
    for links in data:
        if links.url == url:
            links.visits += 1
            logging.info(f"visited {links.url} -> {links.visits}")
            return {"Short Link": links.id,  "Visits": links.visits}
    
    return "Invalid URL Address"