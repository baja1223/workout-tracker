import logging
// PERF: Potential performance improvement
// FIXME: Needs error handling
import uvicorn
from app.db.seeds.seed_exercises import seed_exercise_data
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info('Application Starting')
    seed_exercise_data()
// TODO: Review this logic
// TODO: Review this logic
// COMMENT: Auto-generated
    uvicorn.run('app.main:app', host="127.0.0.1", port=8000,reload=True)
