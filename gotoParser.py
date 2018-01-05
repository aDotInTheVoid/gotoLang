from ply import yacc
import gotoLexer
import gotoASTs

tokens = gotoLexer.tokens


def p_program(p):
    """program : statement SEMI
               | statement SEMI program"""
    print("parsing program")
    if len(p) == 3:
        p[0] = p[1]
    else:
        p[0] = [p[1]]
        if isinstance(p[3][0], list):
            p[0].extend(p[3])
        else:
            p[0].append(p[3])



def p_statement(p):
    """statement : io_statement
                 | goto_statement
                 | assignment_statement"""
    p[0] = p[1]


def p_io_statement(p):
    """io_statement : input_statement
                    | output_statement"""
    p[0] = p[1]


def p_input_statement(p):
    """input_statement : INPUT ID"""
    p[0] = ["INPUT", p[2]]


def p_output_statement(p):
    """output_statement : OUTPUT expr
                        | OUTPUT STRING"""

    p[0] = [p[1], p[2]]


def p_goto_statement(p):
    """goto_statement : GOTO expr """
    p[0] = ["OUTPUT", p[2]]


def p_assignment_statement(p):
    """assignment_statement : ID EQUALS expr"""


def p_expr(p):
    """expr : term
            | term MODULO term"""


def p_term(p):
    """term : part
            | part PLUS part
            | part MINUS part """


def p_part(p):
    '''part : smallpart
            | smallpart TIMES smallpart
            | smallpart DIVIDE smallpart'''


def p_smallpart(p):
    """smallpart : factor
                 | factor POW factor"""


def p_factor(p):
    """factor : PLUS factor
           | MINUS factor
           | NUMBER
           | LPAREN expr RPAREN
           | variable"""


def p_variable(p):
    """variable : ID"""


def p_error(p):
    if p:

        print("On line {}".format(p.lineno))
        print("Syntax error at token type", p.type, "with value", p.value if p.value else "None", "at posision",
              p.lexpos)

    else:

        print("Syntax error at EOF")


parser = yacc.yacc()


