from sqladmin import ModelView
from models.user_models import User, Role


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email]


class RoleAdmin(ModelView, model=Role):
    column_list = [Role.id, Role.name, Role.role_type]