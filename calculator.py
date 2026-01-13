from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Simple Calculator</h2>
    <form method="post" action="/calculate">
        <input name="num1" type="number" required>
        <input name="num2" type="number" required><br><br>
        <select name="operation">
            <option value="add">Add</option>
            <option value="sub">Subtract</option>
            <option value="mul">Multiply</option>
            <option value="div">Divide</option>
        </select><br><br>
        <button type="submit">Calculate</button>
    </form>
    '''
    
@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form['num1'])
    b = float(request.form['num2'])
    op = request.form['operation']

    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        result = a / b if b != 0 else "Error"

    return f"<h3>Result: {result}</h3><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
