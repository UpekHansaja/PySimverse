import cv2
from pysimverse import Drone
import time

drone = Drone()
drone.connect()
drone.streamon()
time.sleep(5)
drone.take_off()
time.sleep(1)

while True:
    print(drone.get_frame())

drone.land()
drone.streamoff()
cv2.destroyAllWindows()
