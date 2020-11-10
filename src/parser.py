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
    value    : STRING
             | NUMBER
    """

    tokens = {STRING, NUMBER}  # type: ignore # noqa: F821

    STRING = r"[a-zA-Z_][a-zA-Z0-9_]*"
    NUMBER = r"\d+"

    ignore = " \t"

    @_(r"\n+")  # type: ignore # noqa: F821
    def newline(self, t) -> None:
        self.lineno += t.value.count("\n")

    def error(self, t) -> None:
        print("Illegal character '%s'" % t.value[0])
        self.index += 1


class SampleParser(Parser):
    tokens = SampleLexer.tokens

    @_("STRING")  # type: ignore # noqa: F821
    def value(self, p) -> Node:
        return Node(type="STRING", body=p.STRING)

    @_("NUMBER")  # type: ignore # noqa: F821
    def value(self, p) -> Node:  # noqa: F811
        return Node(type="NUMBER", body=int(p.NUMBER))


if __name__ == "__main__":
    query = "aaa"
    logger.debug("query={0}".format(query))
    lexer = SampleLexer()
    parser = SampleParser()
    ast = parser.parse(lexer.tokenize(query))
    logger.debug(ast)
