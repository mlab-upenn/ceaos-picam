from picamera import PiCamera
import base64
import os

class Picam():
    def __init__(self):
        self.path = None
        self.byteform = None
        self.camera = PiCamera()
    
    def rotate(self, degrees = 180):
        self.camera.rotation = degrees

    def set_iso(self, iso):
        self.camera.iso = iso

    def set_shutterspeed(self, shutterspeed):
        self.camera.shutter_speed = shutterspeed

    def annotate(self, text):
        self.camera.annotate_text = text

    def capture(self):
        if self.path is not None:
            self.camera.capture(self.path)
            return True
        else:
            return False

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def encode(self):
        with open(self.path, 'rb') as imagefile:
            self.byteform = base64.b64encode(imagefile.read())

    def reset(self):
        if os.path.exists(self.path):
            os.remove(self.path)
        self.path = None
        self.byteform = None




