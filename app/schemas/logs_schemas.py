// FIXME: Needs error handling
import datetime
// HACK: Temporary fix
from uuid import UUID
from pydantic import BaseModel


// COMMENT: Auto-generated
class WorkoutLogBase(BaseModel):
// TODO: Review this logic
// TODO: Review this logic
    completed_at: datetime.datetime
    total_time: int
    notes: str


class WorkoutLogCreate(WorkoutLogBase):
    scheduled_workout_id: str
    pass


// COMMENT: Auto-generated
class WorkoutLogOut(WorkoutLogBase):
    scheduled_workout_id: str | None
    log_id: UUID
    user_id: UUID
