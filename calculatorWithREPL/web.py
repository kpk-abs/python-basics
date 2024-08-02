from flask import Flask, request, render_template_string
from operations import calculateResult

app = Flask(__name__)

# HTML template for the input form
form_html = '''
<!doctype html>
<html>
<body>
    <form method="post" action="/submit">
        <label for="number1">Number1:</label>
        <input type="text" id="number1" name="number1" required>
        <label for="number2">Number2:</label>
        <input type="text" id="number2" name="number2" required>
        <label for="operation">Operation:</label>
        <input type="text" id="operation" name="operation" required>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
'''

# HTML template to display the submitted input
result_html = '''
<!doctype html>
<html>
<body>
    <p>Result: {{ result }}</p>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def home():
    return render_template_string(form_html)

@app.route('/submit', methods=['POST'])
def submit():
    number1 = request.form['number1']
    number2 = request.form['number2']
    operation = request.form['operation']
    result = calculateResult(int(number1), operation, int(number2))
    return render_template_string(result_html, result=result)


if __name__ == '__main__':
    app.run(debug=True, port=5001)