import json
from collections.abc import Callable
from dataclasses import dataclass, fields

raw = '{"name":"this is name","age":10}'

data = json.loads(raw)


@dataclass
class ResponseModel:
    name: str
    age: int


@dataclass
class JSONSerializer:
    model_class: Callable

    def serialize(self, data: dict):
        properties = (data.get(field.name) for field in fields(ResponseModel))
        return self.model_class(*properties)


serialized = JSONSerializer(ResponseModel).serialize(data)
print(serialized)
