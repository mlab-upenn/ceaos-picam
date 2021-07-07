from picamera import PiCamera
import base64
import os

class Picam():
    def __init__(self):
        self.path = None    #Path of local image storage
        self.byteform = None    #64-bit encoded image
        self.camera = PiCamera()    #Set PiCam
    
    def rotate(self, degrees = 180):    #Rotate camera
        self.camera.rotation = degrees

    def set_iso(self, iso): #Set ISO (high ISO for low-light conditions)
        self.camera.iso = iso

    def set_shutterspeed(self, shutterspeed):   #Set shutter speed
        self.camera.shutter_speed = shutterspeed

    def annotate(self, text):   #Annotate images captured by PiCam
        self.camera.annotate_text = text

    def capture(self):  #Capture image
        if self.path is not None:
            self.camera.capture(self.path)
            return True
        else:
            return False

    def set_path(self, path):   #Set path of local image storage
        self.path = path

    def get_path(self): #Returns path of local image storage
        return self.path

    def encode(self):   #Encode image in 64-bit format
        with open(self.path, 'rb') as imagefile:
            self.byteform = base64.b64encode(imagefile.read())
        return self.byteform

    def reset(self):    #Reset camera and delete locally stored image
        if os.path.exists(self.path):
            os.remove(self.path)
        self.path = None
        self.byteform = None




