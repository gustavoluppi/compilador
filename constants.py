from enum import Enum

RESERVED_WORDS = ['if','while','for','return','int','char','else']

SEPARATORS = ['(', ')', '{', '}', '[', ']', ';', ',']

REL_OP = ['<', '>', '==', '!=', '<=', '>=', '=']

LOGIC_OP = ['&&', '||']

BIN_OPS = ['+', '-', '*', '/']





ALL_ELEMENTS = BIN_OPS + REL_OP + LOGIC_OP + SEPARATORS

OPERATORS = {
    '+': 'SUM',
    '-': 'SUB',
    '': 'MUL',
    '/': 'DIV',
    '<': 'LT',
    '>': 'GT',
    '==': 'EQ',
    '!=': 'NE',
    '<=': 'LE',
    '>=': 'GE',
    '=': 'ATTR',
    '&&': 'AND',
    '||': 'OR',
    '(': 'OPEN_BRACKET',
    ')': 'CLOSE_BRACKET',
    '{': 'OPEN_BRACE',
    '}': 'CLOSE_BRACE',
    '[': 'OPEN_SQUARE_BRACKET',
    ']': 'CLOSE_SQUARE_BRACKET',
    ';': 'SEMICOLON',
    ',': 'COMMA',
    'int': 'INT',
    'char': 'CHAR',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'return': 'RETURN',
    '/*': 'OPEN_COMMENT',
    '*/': 'CLOSE_COMMENT',
}


class STATES(Enum):
    INITIAL = 0
    COMMENT = 1
    IDENTIFIER = 2
    LITERAL = 3
    NUMERIC = 4


