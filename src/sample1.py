import json
from collections.abc import Callable, Generator
from dataclasses import dataclass, fields
import pprint

# step1: raw json strings
raw: str = '{"name":"this is name","age":10}'

# step2: raw to json
data: dict = json.loads(raw)


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

    def serialize(self, data: dict) -> Model:
        properties = (data.get(field.name) for field in fields(ResponseModel))
        return self.model_class(*properties)


response_model = JSONSerializer(ResponseModel).serialize(data)
print(response_model)


# Step4: Entity
@dataclass
class UserEntity:
    name: str
    age: int


def to_entity(model: Model) -> Generator:
    return (getattr(model, field.name) for field in fields(model))


entity = UserEntity(*to_entity(response_model))
pprint.pprint(entity)
