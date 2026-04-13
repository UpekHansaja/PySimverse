from pysimverse import Drone
import cv2
import time

drone = Drone()
drone.connect()
drone.streamon()
time.sleep(5)
drone.take_off()
time.sleep(1)

while True:
    frame = drone.get_frame()
    cv2.imwrite("frame.jpg", frame)

drone.land()
drone.streamoff()
cv2.destroyAllWindows()
