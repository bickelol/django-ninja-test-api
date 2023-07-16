from datetime import date
from typing import List
from ninja import NinjaAPI, Schema
from ninja.parser import Parser
from django.shortcuts import get_object_or_404
from .models import Location
from .schemas import LocationIn, LocationOut, LocationSchema, ErrorSchema, JSONHandler
from datetime import datetime
import orjson


class ORJSONParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)


api = NinjaAPI(parser=ORJSONParser()) # NinjaAPI()  # 


@api.post("/locations", response={200: LocationOut, 404: ErrorSchema})
def create_location(request, payload: LocationIn):
    instance = Location.objects.create(**payload.dict())
    print('instance', instance)
    return instance


@api.get("/locations/{location_id}", response=LocationOut)
def get_location(request, location_id: int):
    instance = get_object_or_404(Location, id=location_id)
    return {"data": instance, "success": True}


@api.get("/locations", response=List[LocationOut])
def list_locations(request):
    qs = Location.objects.all()
    return qs # {"data": qs, "success": True}


@api.put("/locations/{location_id}")
def update_location(request, location_id: int, payload: LocationIn):
    instance = get_object_or_404(Location, id=location_id)
    for attr, value in payload.dict().items():
        setattr(Location, attr, value)
    instance.save()
    dict_data = JSONHandler(instance).obj_to_dict()
    return {"data": dict_data, "success": True, "status": 200}


@api.delete("/locations/{location_id}")
def delete_location(request, location_id: int):
    instance = get_object_or_404(Location, id=location_id)
    instance.delete()
    return {"data": "Element deleted", "success": True}
