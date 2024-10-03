import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Car
from .serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(car_json: bytes) -> Car:
    stream = io.BytesIO(car_json)
    data = JSONParser().parse(stream)
    return Car(**data)
