from machine import Pin, PWM
import time

servo_litlle = PWM (Pin(23), freq = 50)
servo_ring = PWM (Pin(18), freq = 50)
servo_middle = PWM (Pin(2), freq = 50)
servo_index = PWM (Pin(4), freq = 50)
servo_thumb = PWM (Pin(19), freq = 50)


def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def litlle():
    servo_litlle.duty(map(0, 0, 180, 10, 180))
    for i in range(0, 181, 10):
        servo_litlle.duty(map(i, 0, 180, 10, 180 ))
        time.sleep(0.3)
        
def ring():
    servo_ring.duty(map(0, 0, 180, 10, 180))
    for i in range(0, 181, 10):
        servo_ring.duty(map(i, 0, 180, 10, 180 ))
        time.sleep(0.3)
        
        
def middle():
    servo_middle.duty(map(0, 0, 180, 10, 180))
    for i in range(0, 181, 10):
        servo_middle.duty(map(i, 0, 180, 10, 180 ))
        time.sleep(0.3)

def index():
    servo_index.duty(map(0, 0, 180, 10, 180))
    for i in range(0, 181, 10):
        servo_index.duty(map(i, 0, 180, 10, 180 ))
        time.sleep(0.3)
        
def thumb():
    servo_thumb.duty(map(0, 0, 180, 10, 180))
    for i in range(0, 181, 10):
        servo_thumb.duty(map(i, 0, 180, 10, 180 ))
        time.sleep(0.3)

while True:
        message =input('Ingrese un la letra: ')
        if message == 'a':
            time.sleep(0.3)
            litlle()
            
        if message == 'b':
            time.sleep(0.3)
            ring()
                
        if message == 'c':
            time.sleep(0.3)
            middle()
            
        if message == 'd':
            time.sleep(0.3)
            index()
            
        if message == 'e':
            time.sleep(0.3)
            thumb()
            
        if message == 'f':
            time.sleep(0.3)
            litlle()
            time.sleep(0.3)
            ring()
            time.sleep(0.3)
            middle()
            time.sleep(0.3)
            index()
            time.sleep(0.3)
            thumb()