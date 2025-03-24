from flask import Flask, render_template, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import datetime
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

application = Flask(__name__)

application.config["JWT_SECRET_KEY"] = "simon"
rate_limiter = Limiter(get_remote_address, app=application, default_limits=["10 per second"])
jwt = JWTManager(application)

LED_CONTROL = 17
BUTTON_CONTROL = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_CONTROL, GPIO.OUT)
GPIO.setup(BUTTON_CONTROL, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_state = {"status": "off"}

MQTT_BROKER = "localhost"
MQTT_TOPIC_LED = "home/led"
MQTT_TOPIC_BUTTON = "home/button"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code " + str(rc))
    client.subscribe(MQTT_TOPIC_LED)

def on_message(client, userdata, msg):
    global led_state
    message = msg.payload.decode()

    if message == "on":
        GPIO.output(LED_CONTROL, GPIO.HIGH)
        led_state["status"] = "on"
        print("LED turned ON via MQTT")
    elif message == "off":
        GPIO.output(LED_CONTROL, GPIO.LOW)
        led_state["status"] = "off"
        print("LED turned OFF via MQTT")

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, 1883, 60)
mqtt_client.loop_start()

@application.route('/')
@rate_limiter.limit("5 per second")
def home():
    return render_template('index.html', led_state=led_state["status"])

@application.route('/generate_token', methods=['POST'])
def generate_token():
    data = request.get_json()
    secret_key = data.get("secret")
    if secret_key == "simon":
        token = create_access_token(identity="user")
        return jsonify({"token": token}), 200
    else:
        return jsonify({"message": "NAROBE!!"}), 401

@application.route('/led/activate', methods=['POST'])
@jwt_required()
def activate_led():
    GPIO.output(LED_CONTROL, GPIO.HIGH)
    led_state["status"] = "on"
    mqtt_client.publish(MQTT_TOPIC_LED, "on")
    return jsonify({"status": led_state["status"]})

@application.route('/led/deactivate', methods=['POST'])
@jwt_required()
def deactivate_led():
    GPIO.output(LED_CONTROL, GPIO.LOW)
    led_state["status"] = "off"
    mqtt_client.publish(MQTT_TOPIC_LED, "off")
    return jsonify({"status": led_state["status"]})

@application.route('/button/check', methods=['GET'])
def check_button():
    button_condition = GPIO.input(BUTTON_CONTROL)
    state = "pritisnjeno" if button_condition == GPIO.LOW else "sprostjeno"
    mqtt_client.publish(MQTT_TOPIC_BUTTON, state)
    return jsonify({"message": state})

@application.route('/led/status', methods=['GET'])
def led_status():
    return jsonify({"status": led_state["status"]})

if __name__ == '__main__':
    try:
        application.run(host='0.0.0.0', port=5000, debug=True)
    finally:
        GPIO.cleanup()

