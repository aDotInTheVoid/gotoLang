import gotoParser
import gotoLexer

programm = """INPUT abc;"""


baseAST = gotoParser.parser().parse(programm, lexer = gotoLexer.lexer)

if not isinstance(baseAST, list):
    baseAST = [baseAST]

print("DONE")
