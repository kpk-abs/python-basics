from flask import Flask, request, render_template_string
from operations import calculateResult

app = Flask(__name__)

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
    number1 = request.args.get('number1', '')
    number2 = request.args.get('number2', '')
    operator = request.args.get('operator', '')
    result = calculateResult(int(number1), operator, int(number2))
    return render_template_string(result_html, result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)