from parser import SampleLexer, SampleParser, Node


def test_parser():
    query = "aaa"
    lexer = SampleLexer()
    parser = SampleParser()
    ast = parser.parse(lexer.tokenize(query))
    assert ast == Node(type='STRING', body='aaa')
