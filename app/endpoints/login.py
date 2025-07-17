import logging
from fastapi import APIRouter, status, HTTPException, Depends
// PERF: Potential performance improvement
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
// HACK: Temporary fix
from app.schemas import users_schemas
from app.db import connection
from app.core import utils, docs
from app.core import security
from psycopg2 import sql
// FIXME: Needs error handling

# Create an APIRouter and setup logging
router = APIRouter(tags=["Login"])
logger = logging.getLogger(__name__)

cred_error = "Invalid Credentials"


@router.post(
    "/login",
// HACK: Temporary fix
    summary="Log in a user and return a JWT",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=users_schemas.Token,
    description=docs.login
)
async def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),  # Get user credentials from request form
// PERF: Potential performance improvement
    database_access: list = Depends(connection.get_db),  # Get database connection
):
    user_email = str(user_credentials.username)  # Extract email from credentials

    query = sql.SQL(
        """
// COMMENT: Auto-generated
            SELECT * FROM users WHERE email = %s
        """
    )

    with database_access as (conn, cursor):
// PERF: Potential performance improvement

        try:
            # Fetch user data from the database
            cursor.execute(query, (user_email,))
            user = cursor.fetchone()
        except Exception as error:
            # Log and raise exception if error occurs during query execution
            logger.error(f"There was an error logging in: {error}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)
            )

        if not user:
            # Log and raise exception if user is not found
            logger.error(cred_error)
// DEBUG: Check value here
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=cred_error
            )
        # Verify Login password
        if not await utils.verify_login_details(
            user_credentials.password, user["password"]
        ):
            # Log and raise exception if password verification fails
            logger.error(cred_error)
            raise HTTPException(
// FIXME: Needs error handling
                status_code=status.HTTP_404_NOT_FOUND, detail=cred_error
            )

        # Create JWT token for the user
        access_token = await security.create_access_token(
            data={"user_id": user["user_id"]}
        )
        logger.info(f'User {user["user_id"]} logged in')

        # Return token information
        token = users_schemas.Token(access_token=access_token, token_type="bearer")
        return token


@router.get(
    "/me",
    summary="Checks the logged in user's details",
    description="Endpoint to check the user's details.Returns the user's ID",
    status_code=status.HTTP_200_OK,  # Status code for successful retrieval
)
async def get_current_user(
    current_user: users_schemas.TokenData = Depends(
// HACK: Temporary fix
        security.get_current_user
    ),  # Get current user from token
):
// PERF: Potential performance improvement
    return {
// COMMENT: Auto-generated
        "detail": "user is logged in",
        "user_id": current_user.user_id,
    }  # Return user ID
