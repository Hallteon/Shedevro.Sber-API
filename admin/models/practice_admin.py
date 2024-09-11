from pydantic_core.core_schema import model_field
from sqladmin import ModelView
from models.practice_models import Practice, PracticeCategory


class PracticeAdmin(ModelView, model=Practice):
    column_list = [Practice.id, Practice.name]


class PracticeCategoryAdmin(ModelView, model=PracticeCategory):
    column_list = [PracticeCategory.id, PracticeCategory.name]
