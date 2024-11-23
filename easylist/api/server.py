from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from scalar_fastapi import get_scalar_api_reference

from .infrastructure.rest.controllers.auth import router_auth
from .infrastructure.rest.controllers.students import router_students
from .infrastructure.rest.controllers.teacher import router_teacher

app = FastAPI(docs_url=None)


@app.get("/docs", include_in_schema=False)
async def docs_scalar_html() -> HTMLResponse:
    return get_scalar_api_reference(openapi_url=app.openapi_url, title=app.title)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_v1_router = APIRouter()

api_v1_router.include_router(router_auth, prefix="/auth", tags=["auth"])
api_v1_router.include_router(router_students, prefix="/students", tags=["students"])
api_v1_router.include_router(router_teacher, prefix="/teacher", tags=["teacher"])

app.include_router(api_v1_router, prefix="/api/v1")
