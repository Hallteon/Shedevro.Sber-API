from fastapi import APIRouter
from api.routes.user_routes import router as user_router
from api.routes.practice_routes import router as practice_router


router = APIRouter()

router.include_router(user_router)
router.include_router(practice_router)