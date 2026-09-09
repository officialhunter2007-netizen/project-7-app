from flask import Flask, jsonify
import time
import threading

is_ready = False

def wait_then_change():
    time.sleep(20)
    global is_ready
    is_ready = True

thread = threading.Thread(target=wait_then_change, daemon=True)
thread.start()

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'project': 'project-7-eks', 'status': 'running','engineer': 'amr'}) ,200
@app.route('/live')
def liveness():
    return jsonify({'status': 'live'}), 200

@app.route('/ready')
def readiness():
    if not is_ready:
        return jsonify({'status': 'not_ready'}), 503
    return jsonify({'status': 'ready'}), 200

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)  # debug=False for production
