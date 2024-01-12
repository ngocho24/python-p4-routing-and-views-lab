from flask import Flask, render_template

app = Flask(__name__)

# Define route for the home page
@app.route('/')
def index():
    return "Python Operations with Flask Routing and Views"


# Define route for the print_string view
@app.route('/print/<string_param>')
def print_string(string_param):
    print(f"String to print: {string_param}")
    return f"String printed: {string_param}"

# Define route for the count view
@app.route('/count/<int:number_param>')
def count(number_param):
    numbers = '\n'.join(str(i) for i in range(number_param + 1))
    return f"Numbers in the range 0 to {number_param}:\n{numbers}"

# Define route for the math view
@app.route('/math/<float:num1>/<string:operation>/<float:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Invalid operation"

    return f"Result of {num1} {operation} {num2} is: {result}"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
