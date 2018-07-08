import parser
import lexer
import interpriter
from docopt import docopt

docstring = """gotoLang.py.

Usage:
    gotoLang.py PROGRAM
    gotoLang.py -h | --help
"""


def run(program):
    parsed_program = parser.parser().parse(program, lexer=lexer.lexer)
    if not isinstance(parsed_program, list):
        parsed_program = [parsed_program]

    runner = interpriter.Interpriter()
    line_num = 0

    while 0 <= line_num < len(parsed_program):
        runner.line_num = line_num
        next_line_num = runner.visit(parsed_program[int(line_num)])

        if next_line_num is not None:
            line_num = next_line_num

        else:
            line_num += 1


if __name__ == "__main__":
    arguments = docopt(docstring, version='gotoLang 1.1')
    run(open(arguments['PROGRAM'], "r").read())
