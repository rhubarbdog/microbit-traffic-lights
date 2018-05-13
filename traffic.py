from microbit import *

red  = pin0
amber= pin1
green= pin2

red_green_time=5000
red_amber_time=1500
amber_time=2500

while True:

    red.write_digital(1)
    sleep(red_green_time)
    
    amber.write_digital(1)
    sleep(red_amber_time)
    
    red.write_digital(0)
    amber.write_digital(0)
    green.write_digital(1)
    sleep(red_green_time)
    
    green.write_digital(0)
    amber.write_digital(1)
    sleep(amber_time)
    
    amber.write_digital(0)
