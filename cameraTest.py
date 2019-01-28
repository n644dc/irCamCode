import time
import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (640, 480)
	camera.framerate = 20
	camera.start_preview()
	time.sleep(1000)