import gotoParser
import gotoLexer
from files import gotoInterpriter

programm = """INPUT a;
INPUT b;
GOTO ((a-b)/((a-b)^2)^0.5)+4;
OUTPUT b;
GOTO 6;
OUTPUT a;
"""
"""OUPUT "HOW MANY NUMBERS";
INPUT numOfNums;
OUTPUT "ENTER THE NUMBERS"
INPUT Largest;
INPUT Another;
LargestGreater = (((Largest-Another)/((Largest-Another)^2)^0.5)+1)/2;
OUTPUT LargestGreater;

"""
parsedProgram = gotoParser.parser().parse(programm, lexer=gotoLexer.lexer)
if not isinstance(parsedProgram, list):
    parsedProgram = [parsedProgram]

interpriter = gotoInterpriter.Interpriter()
lineNum = 0

while 0 <= lineNum < len(parsedProgram):
    nextLineNum = interpriter.visit(parsedProgram[int(lineNum)])
    if nextLineNum is not None:
        lineNum = nextLineNum

    else:
        lineNum += 1


