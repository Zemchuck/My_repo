"""Import necessary modules"""
from flask import Flask, request, jsonify

app=Flask(__name__)# name to specjalna zmienna, która się różni od tego w jaki sposób wykon


@app.route('/') #jeśli ktoś odpyta serwer pod tą scieżką zrób to
def hello_world():  # put application's code here
    """it's a function which return Hello World."""
    return 'Hello Worlds!'
@app.route('/calculate')
def calculate():
    """this function calculates using get function."""
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=float)
    arg2 = request.args.get('arg2', type=float)
    if op is None or arg1 is None or arg2 is None:
        return jsonify({"error": "Brakujące parametry"}), 400
    if op == 'sum':
        result = arg1 + arg2
        op='+'
    elif op == 'sub':
        result = arg1 - arg2
        op='-'
    elif op == 'mul':
        result = arg1 * arg2
        op='*'
    elif op == 'div':
        op='/'
        if arg2 == 0:
            return jsonify({"error": "Dzielenie przez zero"}), 400 #zmiana dict na jsona
        result = arg1 / arg2
    else:
        return jsonify({"error": "Nieznana operacja"}), 400

    # Zwrócenie wyniku
    return str(arg1)+" "+op+" "+str(arg2)+'= '+ str(result)

if __name__ == '__main__':
    app.run(debug=True)
