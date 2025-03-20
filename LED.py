from flask import Flask, render_template, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import RPi.GPIO as GPIO

application = Flask(__name__)
rate_limiter = Limiter(get_remote_address, app=application, default_limits=["10 per second"])

LED_CONTROL = 17
BUTTON_CONTROL = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_CONTROL, GPIO.OUT)
GPIO.setup(BUTTON_CONTROL, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_state = {"status": "off"}

@application.route('/')
@rate_limiter.limit("5 per second")
def home():
    return render_template('index.html', led_state=led_state["status"])

@application.route('/led/activate', methods=['POST'])
def activate_led():
    global led_state
    GPIO.output(LED_CONTROL, GPIO.HIGH)
    led_state["status"] = "on"
    return jsonify({"message": "LED vklopljena", "status": led_state["status"]})

@application.route('/led/deactivate', methods=['POST'])
def deactivate_led():
    global led_state
    GPIO.output(LED_CONTROL, GPIO.LOW)
    led_state["status"] = "off"
    return jsonify({"message": "LED izklopljena", "status": led_state["status"]})

@application.route('/button/check', methods=['GET'])
def check_button():
    button_condition = GPIO.input(BUTTON_CONTROL)
    return jsonify({"message": "pritisnjeno" if button_condition == GPIO.LOW else "sprostjeno"})

@application.route('/led/status', methods=['GET'])
def led_status():
    return jsonify({"status": led_state["status"]})

if __name__ == '__main__':
    try:
        application.run(host='0.0.0.0', port=5000, debug=True)
    finally:
        GPIO.cleanup()
