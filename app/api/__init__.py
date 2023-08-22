from fastapi import APIRouter
from app.api.endpoints import users, reports

router = APIRouter()

router.include_router(users.router, prefix="/safe-drive-ng-api/v1/users", tags=["users"])
router.include_router(reports.router, prefix="/safe-drive-ng-api/v1/reports", tags=["reports"])
