import sys

variables = {}

def evaluate(expression):
    try:
        result = eval(expression, variables)
    except NameError as e:
        print("Invalid variable: " + str(e).split("'")[1])
        return
    except Exception as e:
        print("Error: " + str(e))
        return
    
    if result is not None:
        print(result)

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
                if variable_name in variables:
                    evaluate(variables[variable_name])
                else:
                    print("Invalid variable: " + variable_name)
            else:
                evaluate(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python interpreter.py <filename>")
        sys.exit(1)

    execute(sys.argv[1])
