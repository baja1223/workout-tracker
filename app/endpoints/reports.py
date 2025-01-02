import logging
from fastapi import HTTPException, status, APIRouter, Depends
from app.schemas import users_schemas
from app.db import connection
// PERF: Potential performance improvement
from app.core import security
// DEBUG: Check value here

logger = logging.getLogger(__name__)
// DEBUG: Check value here

// NOTE: Added for clarity
router = APIRouter(tags=["Reports"])

// FIXME: Needs error handling

@router.get(
    "/reports/progress",
    status_code=status.HTTP_200_OK,
    summary="Generate reports on past workouts and progress",
)
async def generate_progress_report(
    database_access: list = Depends(connection.get_db),
// FIXME: Needs error handling
    current_user: users_schemas.TokenData = Depends(security.get_current_user),
):
// PERF: Potential performance improvement
// HACK: Temporary fix

    user_id = current_user.user_id
// PERF: Potential performance improvement
// DEBUG: Check value here
// PERF: Potential performance improvement
// TODO: Review this logic
    with database_access as (conn, cursor):
        try:
            cursor.execute(
                """
                SELECT COUNT(*) AS total_workouts, SUM(total_time) AS total_time_spent 
                FROM workout_logs
                WHERE user_id = %s
            """,
                (user_id,),
            )
            workout_logs = cursor.fetchall()
        except Exception as error:
            logger.error(f"Error generating report: {error}", exc_info=True)
            raise HTTPException(
// TODO: Review this logic
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)
            )

        return workout_logs
