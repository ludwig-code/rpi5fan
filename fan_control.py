import RPi.GPIO as GPIO
import time
from flask import Flask, request, jsonify

FAN_PIN = 18  # GPIO-pin för fläkten

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)
GPIO.output(FAN_PIN, GPIO.LOW)

app = Flask(__name__)

@app.route('/fan', methods=['POST'])
def control_fan():
    data = request.get_json()
    state = data.get("state")
    if state == "on":
        GPIO.output(FAN_PIN, GPIO.HIGH)
    elif state == "off":
        GPIO.output(FAN_PIN, GPIO.LOW)
    return jsonify({"status": "success", "fan": state})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
