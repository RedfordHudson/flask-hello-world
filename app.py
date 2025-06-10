from flask import Flask, request, jsonify

app = Flask(__name__)

# GET route (already there)
@app.route('/')
def hello_world():
    return 'Hello from Flask!'

# NEW: POST route to receive commands
@app.route('/submit', methods=['POST'])
def submit_command():
    try:
        # Grab JSON body
        data = request.get_json()

        # Validate expected keys
        symbol = data.get('symbol')
        action = data.get('action')
        quantity = data.get('quantity')

        if not all([symbol, action, quantity]):
            return jsonify({'error': 'Missing symbol, action, or quantity'}), 400

        # Log or store command (for now just print)
        print(f"Received command: {action} {quantity} shares of {symbol}")

        # Respond with success
        return jsonify({'status': 'success', 'data': data}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
