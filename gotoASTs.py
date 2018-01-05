class AST(object):
    """Parent class for AST Nodes."""

    pass


class BinOp(AST):
    """Binary Operator AST Node. Has 2 CHILDREN."""

    def __init__(self, left, op, right):
        """Save the variables."""
        self.left = left
        self.token = self.op = op
        self.right = right


class UnaryOp(AST):
    """Unary Operator AST node. Has 1 child."""

    def __init__(self, op, expr):
        """Save the variables."""
        self.token = self.op = op
        self.expr = expr


class Num(AST):
    """Number AST Node. Has a value but no children."""

    def __init__(self, token):
        """Save the variables."""
        self.token = token
        self.value = token.value


class Programm(AST):
    def __init__(self):
        self.children = []


class Assign(AST):
    "represents ID ASSIGN expr"
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Var(AST):
    """The Var node is constructed out of ID token."""
    def __init__(self, token):
        self.token = token
        self.value = token.value


class NoOp(AST):
    """Does nothing"""
    pass