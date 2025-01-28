from flask import Flask, jsonify
from control import move_forward, move_backward, turn_left, turn_right, turn_stop

app = Flask(__name__)

@app.route('/move/up', methods=['GET'])
def move_up():
    move_forward()
    return jsonify({"status": "success", "message": "Moved forward"}), 200

@app.route('/move/down', methods=['GET'])
def move_down():
    move_backward()
    return jsonify({"status": "success", "message": "Moved backward"}), 200

@app.route('/move/left', methods=['GET'])
def move_left():
    turn_left()
    return jsonify({"status": "success", "message": "Turned left"}), 200

@app.route('/move/right', methods=['GET'])
def move_right():
    turn_right()
    return jsonify({"status": "success", "message": "Turned right"}), 200

@app.route('/move/stop', methods=['GET'])
def stop_movement():
    turn_stop()
    return jsonify({"status": "success", "message": "Stopped movement"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
