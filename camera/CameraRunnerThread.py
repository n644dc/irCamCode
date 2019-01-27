import os, time
import threading, Queue
import picamera

class CameraRunner(threading.Thread):
    def __init__(self):
      super(CameraRunner, self).__init__()
      self.stoprequest = threading.Event()
      self.camera = picamera.PiCamera()
      time.sleep(2)
      self.camera.resolution = (1640, 1232)
      self.camera.framerate = 20
      print "Camera Successfully Initialized"

    def run(self):
      print "Starting Camera"
      fileName = "feed_" + time.strftime("%a_%d_%b_%Y_%I.%M.%S") + ".h264"
      self.camera.start_recording(fileName, quality=20, bitrate=10000) #750000
      time.sleep(2)
      print "We're rolling!"
      self.camera.wait_recording(8 * 60 * 60)
      self.join()

    def join(self):
        print "And Scene..."
        self.camera.stop_recording()
        super(CameraRunner, self).join(timeout)