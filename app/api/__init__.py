from fastapi import APIRouter
from app.api.endpoints import users, reports,selectedOptions, index

router = APIRouter()
router.include_router(index.router)
router.include_router(selectedOptions.router, prefix="/safe-drive-ng-api/v1/selected_options", tags=["selected_option"])
router.include_router(users.router, prefix="/safe-drive-ng-api/v1/users", tags=["users"])
router.include_router(reports.router, prefix="/safe-drive-ng-api/v1/reports", tags=["reports"])

