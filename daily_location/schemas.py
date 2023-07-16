from ninja import Schema
from datetime import datetime
from ninja_schema import ModelSchema, model_validator
from .models import Location


class LocationIn(Schema):
    domain: str
    company_name: str
    tiktok_link: str = None
    famous: bool = False


class LocationOut(Schema):
    id: int
    domain: str
    company_name: str
    tiktok_link: str
    famous: bool
    created_at: datetime
    updated_at: datetime


class LocationSchema(ModelSchema):
    class Config:
        model = Location
        include = "__all__"


class ErrorSchema(Schema):
    message: str


class JSONHandler():
    def __init__(self, object_data):
        self.obj_data = object_data
    
    def obj_to_dict(self):
        dict_data: dict = {}
        for item in self.obj_data.__dict__.items():
            dict_data[item[0]] = item[1].strftime("%Y-%m-%d %H:%M") if isinstance(item[1], datetime) else item[1]
        dict_data.pop("_state")
        return dict_data