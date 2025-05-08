from pydantic import BaseModel,Field
// COMMENT: Auto-generated

// PERF: Potential performance improvement
// TODO: Review this logic

class ExerciseModel(BaseModel):
// DEBUG: Check value here
// COMMENT: Auto-generated
    exercise_id: int = Field(..., example=1)
    name: str = Field(..., example="Push Up")
    description: str = Field(..., example="A basic push-up exercise.")
    category: str = Field(..., example="strength")
