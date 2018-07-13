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


class NodeVisitor(object):
    """Parent class for classes looking at nodes."""

    def visit(self, node):
        """Input node, call visit function for that paticlar node type."""
        method_name = 'visit_' + type(node).__name__.lower()
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Raise error if no visit method exists for node type."""
        raise Exception('No visit_{} method'.format(type(node.__name__)))


class Interpriter(NodeVisitor):
    """Contains method for looking at spacific gotoLang nodes."""

    def __init__(self):
        """Create a dict for all variables."""
        # TODO: typesystem?
        self.global_scope = dict()

    def visit_assign(self, node):
        """Find the value of the expression and assign it to the variable."""
        var_name = node.left.value
        self.global_scope[var_name] = self.visit(node.right)

    def visit_input(self, node):
        """Input a value and assign it to the variable.

        If the value of the input is a float then cast it to a float
        """
        value = input()

        self.global_scope[node.var.value] = value

    def visit_output(self, node):
        """Print the value of the expression."""
        print(self.visit(node.expr))

    def visit_goto(self, node):
        """Evaluate the expression and return it.

        This is the only function that returns a value (intead of None) which
        allows the run() function in gotolang.py to realise this was a goto
        expression and run the next statement based on the value of the goto.
        """
        return self.visit(node.expr)

    def visit_binop(self, node):
        """Visit and evaluate a BinOP Node."""
        try:
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
            elif node.op == '<':
                return int(self.visit(node.left) < self.visit(node.right))
            elif node.op == '<=':
                return int(self.visit(node.left) <= self.visit(node.right))
            elif node.op == '>':
                return int(self.visit(node.left) > self.visit(node.right))
            elif node.op == '>=':
                return int(self.visit(node.left) >= self.visit(node.right))
            elif node.op == '==':
                return int(self.visit(node.left) == self.visit(node.right))
            elif node.op == '!=':
                return int(self.visit(node.left) != self.visit(node.right)) 
            elif node.op == '&&':
                return int(self.visit(node.left) and self.visit(node.right))
            elif node.op == '||':
                return int(self.visit(node.left) or self.visit(node.right))                            
            else:
                raise NotImplementedError(
                    "No method for binary opperator {}".format(node.op))
        except (ZeroDivisionError, TypeError) as e:
            print("Error on statement {}: {}".format(self.st_num, e))
            exit()

    def visit_unaryop(self, node):
        """Visit and evaluate a UnaryOp."""
        
        if node.op == '+':
            return self.visit(node.expr)
        elif node.op == '-':
            return -self.visit(node.expr)
        elif node.op == 'STR':
            return str(self.visit(node.expr))
        elif node.op == 'INT':
            return int(self.visit(node.expr))
        elif node.op == 'FLOAT':
            return float(self.visit(node.expr))
        elif node.op == 'BOOL':
            return int(bool(self.visit(node.expr)))
        elif node.op == '!':
            return int(not self.visit(node.expr))
        else:
            raise NotImplementedError(
                "No method for unary opperator {}".format(node.op))

    def visit_num(self, node):
        """Return a numbers value."""
        return node.value

    def visit_var(self, node):
        """If a variable exists return the value, otherwise NameError."""
        var_name = node.value
        val = self.global_scope.get(var_name)
        if val is None:
            raise NameError(repr(var_name))
        else:
            return val

    def visit_string(self, node):
        """Return the strings value."""
        return node.value

    def visit_noop(self, node):
        """Do nothing."""
        pass


def getInterpriter():
    """Wraper func needed for consistancy with other modules."""
    return Interpriter()
