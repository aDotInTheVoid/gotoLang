class NodeVisitor(object):
    """Parent class for classes looking at nodes."""

    def visit(self, node):
        """Input node, call visit function for that paticlar node type."""
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Raise error if no visit method exists for node type."""
        raise Exception('No visit_{} method'.format(type(node.__name__)))



class Interpriter(NodeVisitor):
    """Inputs AST, returns integer that that ast evaluates to."""

    def __init__(self):
        """Save the variables."""
        self.global_scope = dict()

    def visit_Assign(self, node):
        var_name = node.left.value
        self.global_scope[var_name] = self.visit(node.right)

    def visit_BinOp(self, node):
        """Visit and evaluate a BinOP Node."""
        if node.op == '+':
            return self.visit(node.left) + self.visit(node.right)
        elif node.op == '-':
            return self.visit(node.left) - self.visit(node.right)
        elif node.op == '*':
            return self.visit(node.left) * self.visit(node.right)
        elif node.op == '/':
            return self.visit(node.left) / self.visit(node.right)
        elif node.op == '%':
            return self.visit(node.left) % self.visit(node.right)
        elif node.op == '^':
            return self.visit(node.left) ** self.visit(node.right)

    def visit_Num(self, node):
        """Return a numbers value."""
        return node.value

    def visit_UnaryOp(self, node):
        """Visit and evaluate a UnaryOp."""
        op = node.op
        if op == "+":
            return self.visit(node.expr)
        else:
            return -self.visit(node.expr)

    def visit_NoOp(self, node):
        pass

    def visit_Var(self, node):
        var_name = node.value
        val = self.global_scope.get(var_name)
        if val is None:
            raise NameError(repr(var_name))
        else:
            return val
