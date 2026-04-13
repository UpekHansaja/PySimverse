from pysimverse import Drone
import time

drone = Drone()
drone.connect()
drone.take_off()

drone.set_speed(80)
time.sleep(1)

# Target 1
drone.move_forward(80)
time.sleep(1)
drone.move_left(300)
time.sleep(1)

#Target 2
drone.move_forward(200)
time.sleep(1)
drone.move_right(300)
time.sleep(1)

# Target 3
drone.move_forward(145)
time.sleep(1)
drone.move_right(340)
time.sleep(1)

drone.land()
time.sleep(1)
