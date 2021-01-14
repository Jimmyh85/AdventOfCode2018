
from sly import Lexer, Parser
import aoc_helper
from functools import reduce
from itertools import product
from collections import defaultdict
import sys

data = aoc_helper.get_input('input18', 'string')
# print(data)


class CalcLexer(Lexer):
    tokens = {NUMBER}
    ignore = " \t"
    literals = {"+", "*", "(", ")"}

    @_(r"\d+")
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    def error(self, t):
        print(f"Illegal character '{t.value[0]}'", file=sys.stderr)
        self.index += 1


class BasicCalcParser(Parser):
    tokens = CalcLexer.tokens
    precedence = (("left", "+", "*"),)

    @_("expr")
    def statement(self, p):
        return p.expr

    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr "*" expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_("NUMBER")
    def expr(self, p):
        return p.NUMBER


class AdvancedCalcParser(Parser):
    tokens = CalcLexer.tokens
    precedence = (
        ("left", "*"),
        ("left", "+"),
    )

    @_("expr")
    def statement(self, p):
        return p.expr

    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr "*" expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_("NUMBER")
    def expr(self, p):
        return p.NUMBER


# Part 1
lexer = CalcLexer()
parser = BasicCalcParser()

sum = 0

for line in data:
    sum += parser.parse(lexer.tokenize(line))

print('Part1: ', sum)

# Part 2
lexer = CalcLexer()
parser = AdvancedCalcParser()

sum = 0

for line in data:
    sum += parser.parse(lexer.tokenize(line))

print('Part:2 ', sum)
