from pysimverse import Drone
import time

drone = Drone()
drone.connect()
drone.take_off()

drone.set_speed(50)
time.sleep(1)

drone.move_forward(320)
time.sleep(1)
drone.move_right(330)
time.sleep(1)

drone.land()
time.sleep(1)
