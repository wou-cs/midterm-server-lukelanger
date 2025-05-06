from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.route('/api/calcs/<value>', methods=['GET'])
def calculate(value):
    try:
        num = int(value)
        if num <= 0:
            abort(404)
    except ValueError:
        abort(404)

    result = {
        "dec": num - 1,
        "hex": hex(num)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

