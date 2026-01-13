from flask import Flask, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
    <style>
        body {
            background: #f2f2f2;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .calculator {
            background: #222;
            padding: 20px;
            border-radius: 10px;
            width: 260px;
            box-shadow: 0px 10px 20px rgba(0,0,0,0.3);
        }

        .display {
            width: 100%;
            height: 50px;
            background: #fff;
            border: none;
            font-size: 22px;
            text-align: right;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
        }

        .buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
        }

        button {
            height: 45px;
            font-size: 18px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .num {
            background: #eee;
        }

        .op {
            background: #ff9500;
            color: white;
        }

        .clear {
            background: #ff3b30;
            color: white;
            grid-column: span 4;
        }
    </style>
</head>
<body>

<div class="calculator">
    <form method="post" action="/calculate">
        <input class="display" type="text" name="expression" value="{{ result }}" readonly>

        <div class="buttons">
            <button class="num" name="btn" value="7">7</button>
            <button class="num" name="btn" value="8">8</button>
            <button class="num" name="btn" value="9">9</button>
            <button class="op" name="btn" value="/">÷</button>

            <button class="num" name="btn" value="4">4</button>
            <button class="num" name="btn" value="5">5</button>
            <button class="num" name="btn" value="6">6</button>
            <button class="op" name="btn" value="*">×</button>

            <button class="num" name="btn" value="1">1</button>
            <button class="num" name="btn" value="2">2</button>
            <button class="num" name="btn" value="3">3</button>
            <button class="op" name="btn" value="-">−</button>

            <button class="num" name="btn" value="0">0</button>
            <button class="num" name="btn" value=".">.</button>
            <button class="op" name="btn" value="=">=</button>
            <button class="op" name="btn" value="+">+</button>

            <button class="clear" name="btn" value="C">CLEAR</button>
        </div>
    </form>
</div>

</body>
</html>
"""

expression = ""

@app.route("/", methods=["GET", "POST"])
def calculator():
    global expression

    if request.method == "POST":
        btn = request.form["btn"]

        if btn == "C":
            expression = ""
        elif btn == "=":
            try:
                expression = str(eval(expression))
            except:
                expression = "Error"
        else:
            expression += btn

    return HTML_TEMPLATE.replace("{{ result }}", expression)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
