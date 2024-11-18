from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from scalar_fastapi import get_scalar_api_reference

from .infrastructure.rest.controllers.students import router_students

app = FastAPI(docs_url=None)


@app.get("/docs", include_in_schema=False)
async def docs_scalar_html() -> HTMLResponse:
    return get_scalar_api_reference(openapi_url=app.openapi_url, title=app.title)


app.include_router(router_students, prefix="/api/v1/students")
