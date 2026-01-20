from flask import Flask, jsonify, request

app = Flask(__name__)

data = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    data.append(item)
    return jsonify({"message": "Item added successfully"}), 201

@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    data.pop(index)
    return jsonify({"message": "Item deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
