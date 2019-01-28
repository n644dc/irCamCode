import time
import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (1280, 720)
	camera.framerate = 30
	camera.start_preview()
	time.sleep(1000)