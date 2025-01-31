from  fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.TablasSQL import Base
from app.api.routes.endpoints import rutas

from starlette.responses import RedirectResponse

#crear las tablas de sql desde python

Base.metadata.create_all(bind=engine)


#variable para administrar la aplicacion
app=FastAPI()

#activar el API

@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)