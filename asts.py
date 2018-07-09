"""asts.py: defines Abstract Syntax Tree classes for gotoLang."""

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


class AST(object):
    """Parent class for AST Nodes."""

    pass


# Statements
class Assign(AST):
    """assignment_statement : var EQUALS expr."""

    def __init__(self, left, op, right):
        """Store variables."""
        self.left = left
        self.op = op
        self.right = right


class Input(AST):
    """input_statement : INPUT var."""

    def __init__(self, var):
        """Store variables."""
        self.var = var


class Output(AST):
    """output_statement : OUTPUT expr."""

    def __init__(self, expr):
        """Store variables."""
        self.expr = expr


class Goto(AST):
    """goto_statement : GOTO expr."""

    def __init__(self, expr):
        """Store variables."""
        self.expr = expr


# Ops
class BinOp(AST):
    """Binary Operator AST Node. Has 2 CHILDREN."""

    def __init__(self, left, op, right):
        """Store variables."""
        self.left = left
        self.op = op
        self.right = right


class UnaryOp(AST):
    """Unary Operator AST node. Has 1 child."""

    def __init__(self, op, expr):
        """Store variables."""
        self.op = op
        self.expr = expr


# Terminals
class Num(AST):
    r"""matches r'[0-9]+(\.[0-9]+)?'."""

    def __init__(self, value):
        """Store variables."""
        self.value = value


class Var(AST):
    """matches r'[a-zA-Z_][a-zA-Z_0-9]*'."""

    def __init__(self, value):
        """Store variables."""
        self.value = value


class String(AST):
    """matches r'[a-zA-Z_][a-zA-Z_0-9]*'."""

    def __init__(self, value):
        """Store variables."""
        self.value = value


class NoOp(AST):
    """Does nothing."""

    pass
