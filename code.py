from adafruit_circuitplayground.express import cpx
import time

OFF = (0, 0, 0)
BLUE = (25, 50, 100)

while True:
    cpx.pixels.fill(BLUE)
    time.sleep(0.5)
    cpx.pixels.fill(OFF)
    time.sleep(0.5)