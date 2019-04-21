# gotoLang
A programing language where the only control flow is ```goto expr```
## Requirements
- Python 3
- Virtualenv 
## Instalation
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
A program is a list of statements seperated by semicolons. Their are 3 types of statements:

- IO Statements
- GOTO Statements
- `assign_statement`

### IO Statements

#### Input
```
INPUT some_var_name
```
Assigns `some_var_name` to a line read from `stdin` exluding the `\n`
#### Output 
```
OUTPUT expr
```
Prints the value of `expr` to `stdout`
### GOTO Statements
```
GOTO expr
```
normaly statements are executed sequentialy. However after the execution of a GOTO Statements, the next statement executed will be the `expr`th statement of the program (starting at 0, of cource). If `expr` is not an integer, or out of range, this is a error.
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
Operators are listed top to bottom, in descending precedence



