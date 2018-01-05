from ply import yacc
import gotoTokens

tokens = gotoTokens.tokens


def p_program(p):
    """program : statement SEMI
               | statement SEMI program"""


def p_statement(p):
    """statement : io_statement
                 | goto_statement
                 | assignment_statement"""


def p_io_statement(p):
    """io_statement : input_statement
                    | output_statement"""


def p_input_statement(p):
    """input_statement : ID EQUALS INPUT"""


def p_output_statement(p):
    """output_statement : OUTPUT EQUALS expr"""


def p_goto_statement(p):
    """goto_statement : GOTO expr"""


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


yacc.yacc()
