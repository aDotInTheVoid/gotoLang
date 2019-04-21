# gotoLang
A programing language where the only control flow is ```goto expr```
## Example program
```
bottles = 99;
s = "s";
OUTPUT (STR) bottles + " bottle" + s + " of beer on the wall,";
OUTPUT (STR) bottles + " bottle" + s + " of beer.";
OUTPUT "Take one down, pass it around,";
bottles = bottles - 1;
s = (bottles > 1) * "s";
GOTO 5 * (bottles == 0) + 8;
OUTPUT (STR) bottles + " bottle" + s + " of beer on the wall.";
OUTPUT "";
GOTO (bottles > 0) + 10;
GOTO 12;
GOTO 2;
OUTPUT "No bottles of beer on the wall.";
```

## Requirements
- Python 3
- Virtualenv 
## Installation
```bash
git clone https://github.com/aDotInTheVoid/gotoLang.git
virtualenv -p python3 venv
source venv/bin/activate
pip3 install ply
```
## Usage
```bash
python3 gotoLang.py path/to/program.goto
```
## Writing Programs
all gotoLang keywords are uppercase. 

### Program Structure
A program is a list of statements separated by semicolons. There are 3 types of statements:

- IO Statements
- GOTO Statements
- `assign_statement`

### IO Statements

#### Input
```
INPUT some_var_name
```
Assigns `some_var_name` to a line read from `stdin` excluding the `\n`
#### Output 
```
OUTPUT expr
```
Prints the value of `expr` to `stdout`
### GOTO Statements
```
GOTO expr
```
normally statements are executed sequentially. However after the execution of a GOTO Statements, the next statement executed will be the `expr`th statement of the program (starting at 0, of course). If `expr` is not an integer, or out of range, this is a error.
### Assign Statements
```
id = expr
```
sets `id` to the value of `expr`
### Writing expressions
#### Primitives
##### Numbers
Must match `r"""[0-9]+(\.[0-9]+)?"""`
Numbers are stored in base 10
##### Strings
Must match `r"""\"([^\\\n]|(\\.))*?\""""`
#### Variables
Must match `r"""[a-zA-Z_][a-zA-Z_0-9]*"""`
### Operators
Operators generally work like c. They can be nested with parenthesis (`(`,`)`).

Operators are listed from highest to lowest precedence.

Operator   | Symbol | Precedence | Associativity
-----------|--------|------------|--------------
Exponential| `^`    | 1          | Right
|||
|||
Unary Plus | `+`    | 2          | None
Unary Minus| `-`    | 2    | None
Logical Not | `!` | 2 | None
|||
|||
Integer Cast | `(INT)` | 3 | None
Bool Cast | `(BOOL)` | 3 | None
Float Cast | `(FLOAT)` | 3 | None
|||
|||
Multiplication | `*` | 4 | Left
Division | `/` | 4 | Left
Modulo | `%` | 4 | Left
|||
|||
Addition | `+` | 5 | Left
Subtraction | `-` | 5 | Left
|||
|||
Less Than | `<` | 6 | Left
Less or Equal | `<=` | 6 | Left
Greater Than | `>` | 6 | Left
Greater or Equal | `>=` | 6 | Left
|||
|||
Equal to| `==` | 7 | Left
Not Equal to | `!=` | 7 | Left 
|||
|||
Logical And | `&&` | 8 | Left
|||
|||
Logical Or | `\|\|`  | 9 | Left
