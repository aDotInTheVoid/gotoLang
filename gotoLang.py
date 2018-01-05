import gotoParser
import gotoLexer
programm = """ OUTPUT "HELLO WORLD"; OUTPUT "HEY"; OUTPUT "3";  """
print(gotoParser.parser.parse(programm, lexer=gotoLexer.lexer))


"""gotoLexer.lexer.input(programm)
for i in gotoLexer.lexer:
    print(i)"""