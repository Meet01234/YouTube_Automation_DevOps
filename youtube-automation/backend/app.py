
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate-blogs', methods=['POST'])
def generate_blogs():
    data = request.get_json()
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({"status": "error", "message": "No prompt provided"}), 400

    # Simulate blog generation
    generated_blogs = [f"{prompt} Blog {i}" for i in range(1, 6)]

    return jsonify({
        "status": "success",
        "message": "Prompt received",
        "blogs": generated_blogs
    }), 200

@app.route('/generate-blogs', methods=['GET'])
def handle_get():
    return jsonify({"message": "Use POST instead of GET"}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
