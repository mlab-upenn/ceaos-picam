from picam import Picam
from time import sleep
from datetime import datetime
import zmq
import json
import os

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.scoket(zmq.REQ)
    socket.connect('tcp://localhost:23267')

    camera = Picam()
    camera.rotate(180)

    json_payload = {}
    while True:
        now = datetime.now()
        date_str = now.strftime("%m_%d_%Y__%H:%M")
        path = '/home/pi/Documents/Plant_Photos/%s.jpg' % date_str
        camera.set_path(path)
        camera.annotate(date_str)
        captured = camera.capture()
        if captured == False:
            print("ERROR: Image capture failed")
            break

        json_payload = {
            'action': 'recv_value',
            'cea-addr': 'farm1.env1.bed1.camera',
            'payload': {"image": camera.encode().decode('ascii')}
        }

        socket.send_json(json_payload)
        message = socket.recv()
        message = json.loads(message)
        print("Received reply %s" % message)

        camera.reset()
        sleep(10800)
