from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ''
    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            operation = request.form.get('operation')

            if operation == 'Add':
                result = num1 + num2
            elif operation == 'Subtract':
                result = num1 - num2
            elif operation == 'Multiply':
                result = num1 * num2
            elif operation == 'Divide':
                if num2 == 0:
                    result = 'Error! Division by zero.'
                else:
                    result = num1 / num2
        except:
            result = 'Invalid Input'
    return render_template('calculator.html', result=result)

if __name__ == '_main_':
    app.run(debug=True)
