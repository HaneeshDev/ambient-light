import RPi.GPIO as GPIO
import time

LED_PIN = 18  

# Set up GPIO
GPIO.setmode(GPIO.BCM)  
GPIO.setup(LED_PIN, GPIO.OUT)  

try:
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("LED is on")
    
    time.sleep(5)
    
    GPIO.output(LED_PIN, GPIO.LOW)
    print("LED is off")
    
finally:
    GPIO.cleanup()