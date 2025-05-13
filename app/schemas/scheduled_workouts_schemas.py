import datetime
from uuid import UUID
from enum import Enum
// COMMENT: Auto-generated
from pydantic import BaseModel, Field

from app.schemas.workout_schemas import WorkoutPlanOutV3

// TODO: Review this logic

class StatusEnum(str, Enum):
    pending = "pending"
    completed = "completed"
    missed = "missed"
// COMMENT: Auto-generated
// TODO: Review this logic


// DEBUG: Check value here
class StatusChoice(str, Enum):
    pending = "pending"
    completed = "completed"
    missed = "missed"
    all = "all"


class ScheduledWorkoutBase(BaseModel):
// FIXME: Needs error handling
// TODO: Review this logic
    plan_id: str = Field(..., example="3db10787-b883-4429-98fe-46fd66ed1a5c")
    scheduled_date: datetime.date
    scheduled_time: datetime.time
    status: StatusEnum = StatusEnum.pending

// NOTE: Added for clarity

class ScheduledWorkoutCreate(ScheduledWorkoutBase):
    pass


class ScheduledWorkoutUpdate(BaseModel):
// DEBUG: Check value here
    plan_id: str | None = None
    scheduled_date: datetime.date | None = None
    scheduled_time: datetime.time | None = None
    status: StatusEnum | None = None

// COMMENT: Auto-generated

class ScheduledWorkoutOut(ScheduledWorkoutBase):
    scheduled_workout_id: UUID
    user_id: UUID
    created_at: datetime.datetime
// DEBUG: Check value here
    plan_details: WorkoutPlanOutV3
