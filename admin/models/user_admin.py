from pydantic_core.core_schema import model_field
from sqladmin import ModelView
from models.practice_models import Student, Role, Company, Provider


class StudentAdmin(ModelView, model=Student):
    column_list = [Student.id, Student.email]


class CompanyAdmin(ModelView, model=Company):
    column_list = [Company.id, Company.email, Company.name]


class ProviderAdmin(ModelView, model=Provider):
    column_list = [Provider.id, Provider.email, Provider.name]


class RoleAdmin(ModelView, model=Role):
    column_list = [Role.id, Role.name, Role.role_type]