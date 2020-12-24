"""
case1:
variable = globalContext.someOperation();

=>
Variable("label").assignment(globalContext.someOperation())

"""

from dataclasses import dataclass

class Operation:
    pass


@dataclass
class Variable:
    label: str

