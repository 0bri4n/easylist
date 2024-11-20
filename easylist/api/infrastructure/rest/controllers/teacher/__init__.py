from fastapi import APIRouter

from .create_teacher import router as create_router_teacher
from .delete_teacher import router as delete_router_teacher
from .get_teacher import router as get_router_teacher
from .update_teacher import router as update_router_teacher

router_teacher = APIRouter()

router_teacher.include_router(create_router_teacher)
router_teacher.include_router(get_router_teacher)
router_teacher.include_router(update_router_teacher)
router_teacher.include_router(delete_router_teacher)
