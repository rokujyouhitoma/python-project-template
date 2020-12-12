from dataclasses import dataclass
import json

raw = '{"name":"this is name"}'

data = json.loads(raw)


class JSONSerializer:
    def serialize(self, data):
        pass


@dataclass
class ResponseModel:
    name: str
