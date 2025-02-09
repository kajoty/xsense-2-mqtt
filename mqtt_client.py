import paho.mqtt.client as mqtt

class MqttClient:
    def __init__(self, broker, port, username, password):
        self.client = mqtt.Client()
        self.client.username_pw_set(username, password)
        self.client.connect(broker, port)

    def publish(self, topic, payload):
        self.client.publish(topic, payload)
