<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Interactive Calculator</title>
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

        input[type="number"] {
            width: 100%;
            padding: 12px 14px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 1.1rem;
            transition: all 0.3s ease;
        }

        input[type="number"]:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 10px rgba(102, 126, 234, 0.2);
            transform: translateY(-1px);
        }

        .operations {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin: 1.8rem 0;
        }

        .operation-btn {
            background: #f8f9fa;
            padding: 14px;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 500;
            border: 2px solid transparent;
            text-align: center;
            user-select: none;
        }

        .operation-btn:hover {
            background: #e9ecef;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }

        .operation-btn.active {
            background: #667eea;
            color: white;
            border-color: #5a6fd9;
            transform: translateY(-1px);
        }

        .calculate-btn {
            width: 100%;
            padding: 14px;
            background: linear-gradient(45deg, #4CAF50, #45a049);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 1.2rem;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 1rem;
            font-weight: 600;
        }

        .calculate-btn:hover {
            background: linear-gradient(45deg, #45a049, #4CAF50);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(76, 175, 80, 0.3);
        }

        .calculate-btn:active {
            transform: translateY(0);
        }

        .result-container {
            margin-top: 2rem;
            opacity: 0;
            transform: translateY(10px);
            transition: all 0.5s ease;
        }

        .result-container.show {
            opacity: 1;
            transform: translateY(0);
        }

        .result-box {
            padding: 1.5rem;
            background: linear-gradient(135deg, #f0f7ff, #e8f4fd);
            border-radius: 10px;
            text-align: center;
            font-size: 1.5rem;
            border-left: 4px solid #667eea;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.1);
        }

        .calculation-display {
            font-size: 1rem;
            color: #666;
            margin-bottom: 0.5rem;
        }

        .result-value {
            color: #333;
            font-weight: bold;
            font-size: 1.8rem;
        }

        .error {
            background: linear-gradient(135deg, #ffebee, #ffcdd2);
            color: #d32f2f;
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            font-weight: 500;
            border-left: 4px solid #d32f2f;
            animation: shake 0.5s ease-in-out;
        }

        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-5px); }
            75% { transform: translateX(5px); }
        }

        .history-container {
            margin-top: 1rem;
            max-height: 200px;
            overflow-y: auto;
        }

        .history-item {
            background: #f8f9fa;
            padding: 8px 12px;
            margin-bottom: 5px;
            border-radius: 6px;
            font-size: 0.9rem;
            color: #555;
            border-left: 3px solid #dee2e6;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .history-item:hover {
            background: #e9ecef;
            border-left-color: #667eea;
        }

        .clear-history {
            background: #dc3545;
            color: white;
            border: none;
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 0.8rem;
            cursor: pointer;
            margin-top: 0.5rem;
            transition: all 0.2s ease;
        }

        .clear-history:hover {
            background: #c82333;
        }
    </style>
</head>
<body>

<div class="calculator-container">
    <h1>Interactive Calculator</h1>

    <div class="form-group">
        <label for="num1">First Number</label>
        <input type="number" id="num1" step="any" placeholder="Enter first number">
    </div>

    <div class="form-group">
        <label for="num2">Second Number</label>
        <input type="number" id="num2" step="any" placeholder="Enter second number">
    </div>

    <div class="operations">
        <div class="operation-btn active" data-operation="add">+ Add</div>
        <div class="operation-btn" data-operation="subtract">− Subtract</div>
        <div class="operation-btn" data-operation="multiply">× Multiply</div>
        <div class="operation-btn" data-operation="divide">÷ Divide</div>
    </div>

    <button class="calculate-btn" onclick="calculate()">Calculate</button>

    <div class="result-container" id="resultContainer">
        <div class="result-box" id="resultBox"></div>
        <div class="history-container" id="historyContainer">
            <button class="clear-history" onclick="clearHistory()" style="display: none;" id="clearBtn">Clear History</button>
        </div>
    </div>
</div>

<script>
    let currentOperation = 'add';
    let calculationHistory = JSON.parse(localStorage.getItem('calculatorHistory')) || [];

    // Initialize
    document.addEventListener('DOMContentLoaded', function() {
        loadHistory();
        setupEventListeners();
    });

    function setupEventListeners() {
        // Operation selection
        document.querySelectorAll('.operation-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                // Remove active class from all buttons
                document.querySelectorAll('.operation-btn').forEach(b => b.classList.remove('active'));
                // Add active class to clicked button
                this.classList.add('active');
                currentOperation = this.getAttribute('data-operation');
            });
        });

        // Real-time calculation on input change
        document.querySelectorAll('input[type="number"]').forEach(input => {
            input.addEventListener('input', function() {
                if (document.getElementById('num1').value && document.getElementById('num2').value) {
                    calculate(false); // Calculate without saving to history
                }
            });
        });

        // Enter key support
        document.querySelectorAll('input[type="number"]').forEach(input => {
            input.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    calculate();
                }
            });
        });
    }

    function calculate(saveToHistory = true) {
        const num1 = parseFloat(document.getElementById('num1').value);
        const num2 = parseFloat(document.getElementById('num2').value);
        const resultContainer = document.getElementById('resultContainer');
        const resultBox = document.getElementById('resultBox');

        // Validation
        if (isNaN(num1) || isNaN(num2)) {
            showError('Please enter valid numbers');
            return;
        }

        if (currentOperation === 'divide' && num2 === 0) {
            showError('Cannot divide by zero!');
            return;
        }

        let result;
        let operationSymbol;

        switch (currentOperation) {
            case 'add':
                result = num1 + num2;
                operationSymbol = '+';
                break;
            case 'subtract':
                result = num1 - num2;
                operationSymbol = '−';
                break;
            case 'multiply':
                result = num1 * num2;
                operationSymbol = '×';
                break;
            case 'divide':
                result = num1 / num2;
                operationSymbol = '÷';
                break;
        }

        // Format result
        result = Math.round(result * 1000000) / 1000000; // Remove floating point errors

        const calculationString = `${num1} ${operationSymbol} ${num2} = ${result}`;

        // Display result
        resultBox.innerHTML = `
            <div class="calculation-display">${num1} ${operationSymbol} ${num2}</div>
            <div class="result-value">${result}</div>
        `;

        resultContainer.classList.add('show');

        // Save to history if this is a manual calculation
        if (saveToHistory) {
            addToHistory(calculationString, { num1, num2, operation: currentOperation, result });
        }
    }

    function showError(message) {
        const resultContainer = document.getElementById('resultContainer');
        const resultBox = document.getElementById('resultBox');
        
        resultBox.innerHTML = `<div class="error">${message}</div>`;
        resultContainer.classList.add('show');
    }

    function addToHistory(calculationString, data) {
        const historyItem = {
            calculation: calculationString,
            data: data,
            timestamp: new Date().toLocaleTimeString()
        };

        calculationHistory.unshift(historyItem); // Add to beginning
        
        // Keep only last 10 calculations
        if (calculationHistory.length > 10) {
            calculationHistory = calculationHistory.slice(0, 10);
        }

        localStorage.setItem('calculatorHistory', JSON.stringify(calculationHistory));
        displayHistory();
    }

    function loadHistory() {
        if (calculationHistory.length > 0) {
            displayHistory();
        }
    }

    function displayHistory() {
        const historyContainer = document.getElementById('historyContainer');
        const clearBtn = document.getElementById('clearBtn');
        
        if (calculationHistory.length === 0) {
            clearBtn.style.display = 'none';
            return;
        }

        clearBtn.style.display = 'block';
        
        // Remove existing history items (but keep clear button)
        const existingItems = historyContainer.querySelectorAll('.history-item');
        existingItems.forEach(item => item.remove());

        calculationHistory.forEach(item => {
            const historyDiv = document.createElement('div');
            historyDiv.className = 'history-item';
            historyDiv.innerHTML = `${item.calculation} <small>(${item.timestamp})</small>`;
            historyDiv.onclick = () => restoreCalculation(item.data);
            historyContainer.insertBefore(historyDiv, clearBtn);
        });
    }

    function restoreCalculation(data) {
        document.getElementById('num1').value = data.num1;
        document.getElementById('num2').value = data.num2;
        
        // Set operation
        document.querySelectorAll('.operation-btn').forEach(btn => {
            btn.classList.remove('active');
            if (btn.getAttribute('data-operation') === data.operation) {
                btn.classList.add('active');
                currentOperation = data.operation;
            }
        });
        
        calculate(false); // Show result without adding to history again
    }

    function clearHistory() {
        calculationHistory = [];
        localStorage.removeItem('calculatorHistory');
        displayHistory();
    }
</script>

</body>
</html>
