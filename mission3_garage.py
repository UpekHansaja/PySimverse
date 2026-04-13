from pysimverse import Drone
import time

drone = Drone()
drone.connect()
drone.take_off()

drone.set_speed(80)
time.sleep(1)

# Target 1
drone.move_forward(450)
time.sleep(1)
drone.move_left(300)
time.sleep(1)

#Target 2
drone.move_down(60)
time.sleep(1)
drone.move_backward(200)
time.sleep(1)
drone.move_right(600)
time.sleep(1)

drone.land()
time.sleep(1)
