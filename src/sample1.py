from dataclasses import dataclass


raw = '{"name":"this is name"}'


@dataclass
class ResponseModel:
    name: str
