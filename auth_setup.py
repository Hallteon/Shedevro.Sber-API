from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

from api.services.auth import *
from models.practice_models import Student, Provider, Company
from settings import config_parameters


cookie_transport = CookieTransport(cookie_name=config_parameters.AUTH_COOKIE_NAME, cookie_max_age=3600,
                                   cookie_secure=True, cookie_samesite='none')


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=config_parameters.AUTH_SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users_students = FastAPIUsers[Student, int](
    get_student_manager,
    [auth_backend],
)

fastapi_users_companies = FastAPIUsers[Company, int](
    get_company_manager,
    [auth_backend],
)

fastapi_users_providers = FastAPIUsers[Provider, int](
    get_provider_db,
    [auth_backend],
)

# current_user = fastapi_users_students.current_user()
