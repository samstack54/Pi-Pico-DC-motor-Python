# DC motor rotation control with TB6612

from machine import Pin, PWM
from utime import sleep

AIN2 = Pin(16, Pin.OUT)
AIN1 = Pin(17, Pin.OUT)
pwm = PWM(Pin(28))

pwm.freq(1000)

def Run_mode(IN1, IN2):
    AIN1.value(IN1)
    AIN2.value(IN2)
    sleep(1)

while True:    
    pwm.duty_u16(35535)  # Max = 65535
    
    Run_mode(1,0)  # Rotate 1 direction
    Run_mode(0,0)  # Stop
    Run_mode(0,1)  # Rotate -1 direction 
    Run_mode(0,0)


