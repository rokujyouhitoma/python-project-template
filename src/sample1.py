import json
from dataclasses import dataclass

raw = '{"name":"this is name"}'

data = json.loads(raw)


@dataclass
class ResponseModel:
    name: str


class JSONSerializer:
    def serialize(self, data):
        return ResponseModel(data.get("name"))


serialized = JSONSerializer().serialize(data)
