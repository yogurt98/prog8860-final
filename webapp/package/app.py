from flask import Flask, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix
from awslambdaric.wsgi import WSGIAdapter

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello_api():
    return jsonify({"message": "Hello, World!"})

# For Lambda: Add WSGI compatibility
def lambda_handler(event, context):
    return WSGIAdapter(app)(event, context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# test pull request