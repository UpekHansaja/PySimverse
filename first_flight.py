from pysimverse import Drone
import time

drone = Drone()
drone.connect()
drone.take_off()

# drone.move_down(20)
# time.sleep(2)
# drone.move_left(40)
# time.sleep(2)
# drone.move_right(60)
# time.sleep(2)

# drone.move_forward(50)
# time.sleep(1)
# drone.move_left(20)
# time.sleep(1)
# drone.move_backward(50)
# time.sleep(1)

# drone.rotate(90)
# time.sleep(1)
# drone.move_forward(50)
# time.sleep(1)
# drone.move_backward(55)
# time.sleep(1)
# drone.rotate(-90)
# time.sleep(1)

drone.set_speed(50)
drone.move_backward(50)
time.sleep(1)
drone.set_speed(150)
drone.move_forward(200)
time.sleep(1)
drone.set_speed(10)
drone.move_backward(100)
time.sleep(1)

drone.land()
time.sleep(1)