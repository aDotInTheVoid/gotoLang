"""gotolang.py: entrypoint for running gotolang programs."""

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


from parser import getParser
from lexer import getLexer
from interpriter import getInterpriter


def run(program):
    """Take a gotolang program (as a string) and runs it."""
    # Generate the abstact syntax tree

    ast = getParser().parse(program, lexer=getLexer())

    # Cast to list
    if not isinstance(ast, list):
        ast = [ast]

    # initialise interpriter
    cmdrunner = getInterpriter()
    statement_pos = 0

    # Mainloop
    while 0 <= statement_pos < len(ast):

        # For error reporing
        cmdrunner.st_num = statement_pos

        # exex statement and find next one
        next_statement_num = cmdrunner.visit(ast[int(statement_pos)])

        # last statement num was not a goto
        if next_statement_num is None:
            statement_pos += 1
        # if it was a goto, then goto there
        else:
            statement_pos = next_statement_num


if __name__ == "__main__":
    import sys
    run(open(sys.argv[1], "r").read())
