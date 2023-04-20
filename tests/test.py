import ast

def add_numbers(a, b):
    return a + b

code = """
def add_numbers(a, b):
    print('Adding numbers:', a, b)
    return a + b + 1
"""

tree = ast.parse(code)
compiled_code = compile(tree, "<string>", "exec")
exec(compiled_code)

result = add_numbers(2, 3)
print(result)  # Output: 6
