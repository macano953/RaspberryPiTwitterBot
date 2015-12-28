#!/bin/python
#script to read a file and extract a number
import os
import paho.mqtt.publish as publish
from json import dumps
class CarriotsMqttClient():
    host = 'mqtt.carriots.com'
    port = '1883'
    auth = {}
    topic = '%s/streams'
    tls = None

    def __init__(self, auth, tls=None):
        self.auth = auth
        self.topic = '%s/streams' % auth['username']
        if tls:
            self.tls = tls
            self.port = '8883'

    def publish(self, msg):
        try:
            publish.single(topic=self.topic, payload=msg, hostname=self.host, auth=self.auth, tls=self.tls, port=self.port)
        except Exception, ex:
            print ex


def getTemp():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
print " Stream uploading in process ".center(75,"=")
auth = {'username': '-', 'password': ''}
#tls_dict = {'ca_certs': 'ca_certs.crt', 'tls_version': PROTOCOL_TLSv1}  # ssl version
temp = getTemp()
msg_dict = {'protocol': 'v2', 'device': 'RPi@miguelcano953.miguelcano953', 'at': 'now', 'data': {'temp': temp}}
client_mqtt = CarriotsMqttClient(auth=auth)                     # non ssl version
#client_mqtt = CarriotsMqttClient(auth=auth, tls=tls_dict)      # ssl version
client_mqtt.publish(dumps(msg_dict))
print " Upload complete! ".center(75, "=")
