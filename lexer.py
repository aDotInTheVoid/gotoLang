"""lexer.py: tokenises gotoLang source code."""

# Copyright 2017, 2018 Nixon Enraght-Moony

# This file is part of gotoLang.

# gotoLang is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3
# as published by the Free Software Foundation

# gotoLang is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with gotoLang.  If not, see <https://www.gnu.org/licenses/>.

import ply

reserved = {
    'INPUT': 'INPUT',
    'OUTPUT': 'OUTPUT',
    'GOTO': 'GOTO'
}

tokens = [
    # Literals (identifier, float constant, string constant)
    'ID', 'NUMBER', 'STRING',

    # Operators (+,-,*,/,%,^)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO', 'POW',

    # Assignment (=)
    'EQUALS',

    # Delimeters ((, ))
    'LPAREN', 'RPAREN',

    # End of statement (;)
    'SEMI',
] + list(reserved.values())

t_ignore = ' \t'


# Yes i Know this violates PEP8/PEP257 but its neaded to work with PLY
def t_ID(t):  
    r"""[a-zA-Z_][a-zA-Z_0-9]*"""
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_POW = r'\^'

t_EQUALS = r'='

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'

t_INPUT = r'INPUT'
t_OUTPUT = r'OUTPUT'
t_GOTO = r'GOTO'

t_ignore_COMMENT = r'\#.*'


# Yes i Know this violates PEP8/PEP257 but its neaded to work with PLY
def t_NUMBER(t):
    r"""[0-9]+(\.[0-9]+)?"""
    t.value = float(t.value)
    return t


# Yes i Know this violates PEP8/PEP257 but its neaded to work with PLY
def t_STRING(t):
    r"""\"([^\\\n]|(\\.))*?\""""  # I think this is right ...
    t.value = t.value[1:-1]
    return t


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


def t_error(t):
    """Raise an error when you cant lex."""
    # TODO: More usefull errors
    print("Illegal character '%s'" % t.value[0])


def getLexer():
    """Return a lexer with the tokens we set up."""
    return ply.lex.lex()
