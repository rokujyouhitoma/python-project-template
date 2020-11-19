import dataclasses
import logging
import typing

from sly import Lexer, Parser  # type: ignore

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@dataclasses.dataclass
class Node:
    type: str
    body: typing.List["Node"]


class SampleLexer(Lexer):
    """
    Grammar.
    statement: value
             | LBRACKET variable RBRACKET
    value    : STRING
             | NUMBER
    variable : STRING
    """

    ignore = " \t"

    tokens = {STRING, NUMBER, LBRACKET, RBRACKET}  # type: ignore # noqa: F821

    STRING = r"[a-zA-Z_][a-zA-Z0-9_]*"
    NUMBER = r"\d+"

    LBRACKET = r"{"
    RBRACKET = r"}"

    @_(r"\n+")  # type: ignore # noqa: F821
    def newline(self, t) -> None:
        self.lineno += t.value.count("\n")


class SampleParser(Parser):
    tokens = SampleLexer.tokens

    @_("value")  # type: ignore # noqa: F821
    def statement(self, p):  # noqa: F811
        return p.value

    @_("LBRACKET variable RBRACKET")  # type: ignore # noqa: F821
    def statement(self, p):  # noqa: F811
        return p.variable

    @_("STRING")  # type: ignore # noqa: F821
    def value(self, p) -> Node:
        return Node(type="STRING", body=p.STRING)

    @_("NUMBER")  # type: ignore # noqa: F821
    def value(self, p) -> Node:  # noqa: F811
        return Node(type="NUMBER", body=int(p.NUMBER))

    @_("STRING")  # type: ignore # noqa: F821
    def variable(self, p) -> Node:
        return Node(type="VARIABLE", body=p.STRING)
