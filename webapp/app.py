from flask import Flask, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello_api():
    return jsonify({"message": "Hello, World!"})

# For Lambda: Add WSGI compatibility
def lambda_handler(event, context):
    from awslambdaric.wsgi import WSGIAdapter
    return WSGIAdapter(app)(event, context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Test 