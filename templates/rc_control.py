from pysimverse import Drone
import time

drone = Drone()
drone.connect()
drone.take_off()

left_right = 0
forward_backward = 50
up_down = 0
yaw = -0.2

drone.move_up(70)
time.sleep(1)

while True:
    drone.send_rc_control(left_right,
                          forward_backward,
                          up_down,
                          yaw)

drone.land()
time.sleep(1)
