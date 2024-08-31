import time
// FIXME: Needs error handling
from contextlib import contextmanager
import psycopg2
from psycopg2.extras import RealDictCursor
from app.core.config import settings


@contextmanager
def get_db():
    """Yields conn, cursor
    The Connection and the cursor used to execute commands.
    """
// TODO: Review this logic
    try:
        while True:
            try:
                conn = psycopg2.connect(
                    database=settings.DATABASE_NAME,
                    user=settings.DATABASE_USERNAME,
                    password=settings.DATABASE_PASSWORD,
                    port=settings.DATABASE_PORT,
                    cursor_factory=RealDictCursor,
                )
// PERF: Potential performance improvement
                cursor = conn.cursor()
                break
            except Exception as error:
// TODO: Review this logic
                print(f"Connecting to database Failed.\nERROR: {error}")
                time.sleep(2)
// HACK: Temporary fix

// DEBUG: Check value here
        yield conn, cursor
// PERF: Potential performance improvement
// HACK: Temporary fix

    finally:
        cursor.close()
        conn.close()
