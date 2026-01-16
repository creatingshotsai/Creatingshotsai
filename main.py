from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze-video', methods=['POST'])
def analyze():
    return jsonify({
        "status": "success",
        "category": "Entertainment/Comedy",
        "trending_tags": ["#viral", "#shorts", "#trending"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
  
