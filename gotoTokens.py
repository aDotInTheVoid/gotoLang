import ply.lex as lex

tokens = [
    # Literals (identifier, float constant, string constant)
    'ID', 'NUMBER', 'STRING',

    # Operators (+,-,*,/,%,^)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO', 'POW',
    # (|,&,~)
    'OR', 'AND', 'NOT',
    # (<, <=, >, >=, ==, !=)
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

    # Assignment (=)
    'EQUALS',

    # Delimeters ( ) ;
    'LPAREN', 'RPAREN',

    'SEMI',

    # IO
    'INPUT', 'OUTPUT',

    # Controll flow
    'GOTO'
]

t_ignore = ' \t'

t_ID = r'[A-Za-z_][A-Za-z0-9_]*'
t_STRING = r'\"([^\\\n]|(\\.))*?\"'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_POW = r'\^'

t_OR = r'\|'
t_AND = r'&'
t_NOT = r'!'

t_EQUALS = r'='

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'

t_INPUT = r'INPUT'
t_OUTPUT = r'OUTPUT'
t_GOTO = r'GOTO'


def t_NUMBER(t):
    r'[0-9]+(\.[0-9]+)?'
    t.value = float(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


lex.lex()
