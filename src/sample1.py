import json
from collections.abc import Callable
from dataclasses import dataclass, fields

# step1: raw
raw = '{"name":"this is name","age":10}'

# step2: raw to json
data = json.loads(raw)


# step3: json to model
@dataclass
class Model:
    pass


@dataclass
class ResponseModel(Model):
    name: str
    age: int


@dataclass
class JSONSerializer:
    model_class: Callable

    def serialize(self, data: dict):
        properties = (data.get(field.name) for field in fields(ResponseModel))
        return self.model_class(*properties)


response_model = JSONSerializer(ResponseModel).serialize(data)
print(response_model)


# Step4: Entity
@dataclass
class UserEntity:
    name: str
    age: int


def to_entity(model):
    return (getattr(model, field.name) for field in fields(model))


entity = UserEntity(*to_entity(response_model))
print(entity.name)
print(entity.age)
