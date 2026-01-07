<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Simple Calculator</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .calculator-container {
            background: white;
            padding: 2.5rem 2rem;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            width: 100%;
            max-width: 420px;
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 1.8rem;
            font-size: 2rem;
        }

        .form-group {
            margin-bottom: 1.4rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            color: #444;
            font-weight: 500;
        }

        input[type="number"],
        input[type="text"] {
            width: 100%;
            padding: 12px 14px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 1.1rem;
            transition: border-color 0.2s;
        }

        input[type="number"]:focus,
        input[type="text"]:focus {
            outline: none;
            border-color: #667eea;
        }

        .operations {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin: 1.8rem 0;
        }

        .operations label {
            display: flex;
            align-items: center;
            justify-content: center;
            background: #f8f9fa;
            padding: 14px;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.2s;
            font-weight: 500;
            border: 2px solid transparent;
        }

        .operations input[type="radio"] {
            display: none;
        }

        .operations input[type="radio"]:checked + label {
            background: #667eea;
            color: white;
            border-color: #5a6fd9;
        }

        button {
            width: 100%;
            padding: 14px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 1.2rem;
            cursor: pointer;
            transition: background 0.2s;
            margin-top: 1rem;
        }

        button:hover {
            background: #43a047;
        }

        .result-box {
            margin-top: 2rem;
            padding: 1.2rem;
            background: #f0f7ff;
            border-radius: 10px;
            text-align: center;
            font-size: 1.5rem;
            min-height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .error {
            color: #d32f2f;
            text-align: center;
            margin-top: 1rem;
            font-weight: 500;
        }
    </style>
</head>
<body>

<div class="calculator-container">
    <h1>Basic Calculator</h1>

    <form method="POST">
        <div class="form-group">
            <label for="num1">First Number</label>
            <input type="number" id="num1" name="num1" step="any" 
                   value="{{ num1 }}" placeholder="e.g. 42" required>
        </div>

        <div class="form-group">
            <label for="num2">Second Number</label>
            <input type="number" id="num2" name="num2" step="any" 
                   value="{{ num2 }}" placeholder="e.g. 7" required>
        </div>

        <div class="operations">
            <input type="radio" id="add" name="operation" value="add" 
                   {% if operation == 'add' or not operation %}checked{% endif %}>
            <label for="add">+ Add</label>

            <input type="radio" id="subtract" name="operation" value="subtract"
                   {% if operation == 'subtract' %}checked{% endif %}>
            <label for="subtract">− Subtract</label>

            <input type="radio" id="multiply" name="operation" value="multiply"
                   {% if operation == 'multiply' %}checked{% endif %}>
            <label for="multiply">× Multiply</label>

            <input type="radio" id="divide" name="operation" value="divide"
                   {% if operation == 'divide' %}checked{% endif %}>
            <label for="divide">÷ Divide</label>
        </div>

        <button type="submit">Calculate</button>
    </form>

    {% if error %}
        <div class="error">{{ error }}</div>
    {% endif %}

    {% if result is not none %}
        <div class="result-box">
            Result: <strong>{{ result }}</strong>
        </div>
    {% endif %}
</div>

</body>
</html>
