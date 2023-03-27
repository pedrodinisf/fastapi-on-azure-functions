import logging
import azure.functions as func
from FastAPIApp import app  # Main API application
from GDA import utils

@app.get("/sample")
async def index():
    filename = utils.get_tmp_filename(".xlsx")
    return {
        "info": filename,
    }


@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req, context)
