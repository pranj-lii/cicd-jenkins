import math
import os

DATA_DIR = "/app/data"
HISTORY_FILE = os.path.join(DATA_DIR, "history.txt")

# Create data directory if not exists
os.makedirs(DATA_DIR, exist_ok=True)

def save_history(entry):
    with open(HISTORY_FILE, "a") as f:
        f.write(entry + "\n")

def calculator():
    print("Scientific Calculator")
    print("Type 'exit' to quit\n")

    while True:
        expression = input("Enter operation: ")

        if expression.lower() == "exit":
            print("Exiting calculator.")
            break

        try:
            # Allowed safe functions
            allowed_names = {
                "sin": math.sin,
                "cos": math.cos,
                "sqrt": math.sqrt,
                "log": math.log
            }

            result = eval(expression, {"__builtins__": None}, allowed_names)
            print("Result:", result)

            save_history(f"{expression} = {result}")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    calculator()
