"""interpriter.py: interprites gotoLang Abstract Syntax Trees."""

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

import sys

from ply import yacc

import asts
import lexer

tokens = lexer.tokens


# Top level AST
# TODO: make nicer
def p_program(p):
    """program : statement SEMI
               | statement SEMI program
    """
    if len(p) == 3:
        p[0] = p[1]
    else:
        p[0] = [p[1]]
        if isinstance(p[3], list):

            p[0].extend(p[3])

        else:
            p[0].append(p[3])


# Statements
def p_statement(p):
    """statement : io_statement
                 | goto_statement
                 | assignment_statement
                 | none
    """
    p[0] = p[1]


def p_io_statement(p):
    """io_statement : input_statement
                    | output_statement
    """
    p[0] = p[1]


def p_input_statement(p):
    """input_statement : INPUT var"""
    p[0] = asts.Input(p[2])


def p_output_statement(p):
    """output_statement : OUTPUT expr"""
    p[0] = asts.Output(p[2])


def p_goto_statement(p):
    """goto_statement : GOTO expr"""
    p[0] = asts.Goto(p[2])


def p_assignment_statement(p):
    """assignment_statement : var EQUALS expr"""
    p[0] = asts.Assign(p[1], p[2], p[3])


# Expressions and opperators
def p_expr(p):
    """expr : term
            | term MODULO term
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = asts.BinOp(p[1], p[2], p[3])


def p_term(p):
    """term : part
            | part PLUS part
            | part MINUS part
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = asts.BinOp(p[1], p[2], p[3])


def p_part(p):
    """part : smallpart
            | smallpart TIMES smallpart
            | smallpart DIVIDE smallpart
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = asts.BinOp(p[1], p[2], p[3])


def p_smallpart(p):
    """smallpart : factor
                 | factor POW factor
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = asts.BinOp(p[1], p[2], p[3])


def p_factor(p):
    """factor : PLUS factor
           | MINUS factor
           | num
           | str
           | LPAREN expr RPAREN
           | var
    """
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = asts.UnaryOp(p[1], p[2])
    else:
        p[0] = p[2]


# Terminals
def p_variable(p):
    """var : ID"""

    p[0] = asts.Var(p[1])


def p_num(p):
    """num : NUMBER"""
    p[0] = asts.Num(p[1])


def p_str(p):
    """str : STRING"""
    p[0] = asts.String(p[1])


def p_none(p):
    """none :"""
    p[0] = asts.NoOp()


def p_error(p):
    """Reprot an error if one turns up."""
    if p:

        print("On line {}".format(p.lineno), file=sys.stderr)
        print("Syntax error at token type", p.type, "with value", 
              p.value if p.value else "None", "at posision",
              p.lexpos, file=sys.stderr)

    else:

        print("Syntax error at EOF", file=sys.stderr)

    exit(1)


def getParser():
    """Give a parser."""
    return yacc.yacc(debug=True)
