import sys

variables = {}

def evaluate(expression):
    try:
        # Check if expression is a string
        if expression.startswith('"') and expression.endswith('"'):
            return expression[1:-1]
        
        # Check if expression is an integer or float
        if expression.replace('.', '', 1).isdigit():
            return eval(expression)

        # Check if expression is a variable name
        if expression in variables:
            return variables[expression]

        # Otherwise, try evaluating as a Python expression with variables
        return eval(expression, variables)

    except NameError as e:
        raise NameError("Invalid variable: " + str(e))

    except Exception as e:
        raise Exception("Error evaluating expression: " + str(e))


def execute(file):
    with open(file) as f:
        lines = f.readlines()

    for line in lines:
        # Remove any leading/trailing whitespace and newline characters
        line = line.strip()

        # Skip any empty lines or comments
        if not line or line.startswith("//") or line.startswith("#"):
            continue

        # Check for variable assignment
        if line.startswith("var "):
            parts = line.split(" ")
            variable_name = parts[1]
            variable_value = " ".join(parts[3:])
            if variable_value.isnumeric():
                variable_value = int(variable_value)
            variables[variable_name] = variable_value
        else:
            # Check if prnt statement contains a variable
            if "prnt" in line:
                variable_name = line.split(" ")[1]
                try:
                    print(evaluate(variable_name))
                except NameError:
                    if variable_name.startswith('"') and variable_name.endswith('"'):
                        print(variable_name[1:-1])
                    else:
                        print("Invalid variable: " + variable_name)
            else:
                try:
                    evaluate(line)
                except NameError:
                    print("Invalid variable: " + line.split(" ")[1])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python interpreter.py <filename>")
        sys.exit(1)

    execute(sys.argv[1])
