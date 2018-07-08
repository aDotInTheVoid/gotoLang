from ply import yacc
import gotoASTs
import gotoLexer

tokens = gotoLexer.tokens


# Top level AST
def p_program(p):
    """program : statement SEMI
               | statement SEMI program"""

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
                 | none"""
    p[0] = p[1]


def p_io_statement(p):
    """io_statement : input_statement
                    | output_statement"""
    p[0] = p[1]


def p_input_statement(p):
    """input_statement : INPUT var"""
    p[0] = gotoASTs.Input(p[2])


def p_output_statement(p):
    """output_statement : OUTPUT expr"""

    p[0] = gotoASTs.Output(p[2])


def p_goto_statement(p):
    """goto_statement : GOTO expr """
    p[0] = gotoASTs.Goto(p[2])


def p_assignment_statement(p):
    """assignment_statement : var EQUALS expr"""
    p[0] = gotoASTs.Assign(p[1], p[2], p[3])


# Expression & Jazz
def p_expr(p):
    """expr : term
            | term MODULO term"""

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = gotoASTs.BinOp(p[1], p[2], p[3])


def p_term(p):
    """term : part
            | part PLUS part
            | part MINUS part """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = gotoASTs.BinOp(p[1], p[2], p[3])


def p_part(p):
    """part : smallpart
            | smallpart TIMES smallpart
            | smallpart DIVIDE smallpart"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = gotoASTs.BinOp(p[1], p[2], p[3])


def p_smallpart(p):
    """smallpart : factor
                 | factor POW factor"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = gotoASTs.BinOp(p[1], p[2], p[3])


def p_factor(p):
    """factor : PLUS factor
           | MINUS factor
           | num
           | str
           | LPAREN expr RPAREN
           | var"""
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = gotoASTs.UnaryOp(p[1], p[2])
    else:
        p[0] = p[2]


# Terminal
def p_variable(p):
    """var : ID"""

    p[0] = gotoASTs.Var(p[1])


def p_num(p):
    """num : NUMBER"""
    p[0] = gotoASTs.Num(p[1])


def p_str(p):
    """str : STRING"""
    p[0] = gotoASTs.String(p[1])


def p_none(p):
    """none :"""
    p[0] = gotoASTs.NoOp()


def p_error(p):
    if p:

        print("On line {}".format(p.lineno))
        print("Syntax error at token type", p.type, "with value", p.value if p.value else "None", "at posision",
              p.lexpos)

    else:

        print("Syntax error at EOF")


def parser():
    """Give a parser."""
    return yacc.yacc()
