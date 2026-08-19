import pytest

from src.interpreter import Interpreter, Lexer, Parser


def interpret(expression):
    lexer = Lexer(expression)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    return interpreter.interpret()


def test_addition():
    assert interpret("2 + 4 - 5") == 1


@pytest.mark.parametrize(
    "expr,value",
    [
        ["(2 + 3) * 4", 20],
        ["4 * (2 + 3)", 20],
    ],
)
def test_multiplication_with_parentheses(expr, value):
    assert interpret(expr) == value
