class AST(object):
    """Parent class for AST Nodes."""

    pass


class Programm(AST):
    def __init__(self):
        self.children = []


# Statements
class Assign(AST):
    "represents ID ASSIGN expr"

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Input(AST):
    def __init__(self, var):
        self.var = var


class Output(AST):
    def __init__(self, expr):
        self.expr = expr


class Goto(AST):
    def __init__(self, expr):
        self.expr = expr


# Ops
class BinOp(AST):
    """Binary Operator AST Node. Has 2 CHILDREN."""

    def __init__(self, left, op, right):
        """Save the variables."""
        self.left = left
        self.op = op
        self.right = right


class UnaryOp(AST):
    """Unary Operator AST node. Has 1 child."""

    def __init__(self, op, expr):
        """Save the variables."""
        self.op = op
        self.expr = expr


# Terminals
class Num(AST):
    """Number AST Node. Has a value but no children."""

    def __init__(self, value):
        """Save the variables."""

        self.value = value


class Var(AST):
    """The Var node is constructed out of ID token."""

    def __init__(self, value):
        self.value = value


class String(AST):
    def __init__(self, value):
        self.value = value


class NoOp(AST):
    """Does nothing"""
    pass
