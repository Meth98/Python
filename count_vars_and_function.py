# Script that it counts all variables and all functions in the code using the 'ast' library

import ast

code = r'''             # r: to escape '\n' automatically
import os, sys

def func():
    temp = 5

def main():
    x = 2
    y = x
    z = x + "\n" + y

var = "Ciao sono una variabile"
main()
'''

# to extract all variables from code's AST (abstract syntax tree)
tree = ast.parse(code)
variables = []

for node in ast.walk(tree):
    if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
        variable_name = node.id

        if variable_name not in variables:
            variables.append(variable_name)

# count the variables
variable_counts = len(variables)
print(f"Number of variables: {variable_counts}")

# print also all the variables names
for variable in variables:
    print(f"Name: {variable}")

print("----------------")

# to extract all functions from code's AST
tree = ast.parse(code)
function_defs = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

# count the functions
function_counts = len(function_defs)
print(f"Number of functions: {function_counts}")

# print also all the functions names
for function_name in function_defs:
    print(f"Name: {function_name}")