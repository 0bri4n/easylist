from fastapi import APIRouter

from .create_student import router as create_router
from .delete_student import router as delete_router
from .get_student import router as get_router
from .list_students import router as list_router
from .update_student import router as update_router

router_students = APIRouter()

router_students.include_router(create_router)
router_students.include_router(get_router)
router_students.include_router(list_router)
router_students.include_router(update_router)
router_students.include_router(delete_router)
