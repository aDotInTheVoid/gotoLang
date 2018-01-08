from gotoLang import gotoLexer
from gotoLang import gotoParser

programm = """ OUTPUT 2+2;"""

baseAST = gotoParser.parser.parse(programm, lexer=gotoLexer.lexer)

if not isinstance(baseAST, list):
    baseAST = [baseAST]

print("DONE")
