import pytest
from sly.lex import Token as Token_

from parser import SampleLexer, SampleParser, Node


def Token(type, value, lineno, index):
    token = Token_()
    token.type = type
    token.value = value
    token.lineno = lineno
    token.index = index
    return token


class TestLexer:
    @pytest.mark.parametrize(
        "test_input,expected", [
            ("{a}", [
                Token(type='LBRACKET', value='{', lineno=1, index=0),
                Token(type='STRING', value='a', lineno=1, index=1),
                Token(type='RBRACKET', value='}', lineno=1, index=2)
            ]),
        ]
    )
    def test_tokenize(self, test_input, expected):
        lexer = SampleLexer()
        tokens = [token for token in lexer.tokenize(test_input)]
        for v1, v2 in zip(tokens, expected):
            assert v1.type == v2.type
            assert v1.value == v2.value
            assert v1.lineno == v2.lineno
            assert v1.index == v2.index


class TestParser:
    @pytest.mark.parametrize(
        "test_input,expected", [
            ("a", Node(type='STRING', body='a')),
            ("{a}", Node(type='VARIABLE', body='a')),
        ]
    )
    def test_parse(self, test_input, expected):
        lexer = SampleLexer()
        parser = SampleParser()
        node = parser.parse(lexer.tokenize(test_input))
        assert node == expected


def test_parser():
    query = "{a}"
    lexer = SampleLexer()
    parser = SampleParser()
    ast = parser.parse(lexer.tokenize(query))
    assert ast
