import os
import time
import threading
import picamera

class CameraRunner(threading.Thread):
    def __init__(self):
      super(CameraRunner, self).__init__()
      self.stoprequest = threading.Event()
      self.camera = picamera.PiCamera()
      self.fileDir = '/mnt/usb/'
      self.fileName = None
      time.sleep(2)
      self.camera.resolution = (1280, 720)
      self.camera.framerate = 40
      print "Camera Successfully Initialized"

    def run(self):
      self.fileName = "feed_" + time.strftime("%a_%d_%b_%Y_%I.%M.%S")
      camPath = os.path.join(self.fileDir, self.fileName)
      self.camera.start_recording(camPath + ".h264", quality=20, bitrate=10000) #750000
      time.sleep(2)
      print "We're rolling!"
      self.camera.wait_recording(8 * 60 * 60)

    def join(self):
        print "And Scene..."
        self.camera.stop_recording()
        self.camera.close()
        super(CameraRunner, self).join()