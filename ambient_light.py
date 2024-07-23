# RPi.GPIO is pre-installed in Raspberry pi
import RPi.GPIO as GPIO
import time

from weather_data import scrap_weather

# Define LED pin
LED_PIN = 12

# Pin Numbering Declaration
# GPIO.BCM - numbers silkscreened on the PCB
GPIO.setmode(GPIO.BCM) # activate the Broadcom-chip specific pin numbers

# Setting a Pin Mode
GPIO.setup(LED_PIN, GPIO.OUT)


# PWM ("Analog") Output
# PWM( Pulse width modulation ) - generates variable-width pulses to represent the amplitude of an analog input signal.
# Setting GPIO.PWM([pin], [frequency]) to LED_PIN, 1000 Hz - 18, 1 kHz
pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(50) # output - start with 50% duty cycle

def led_brightness(brightness):
    pwm.ChangeDutyCycle(brightness)

def cal_brightness(weather):
    temperature = weather['temperature']
    humidity = weather['humidity']
    precipitation = weather['precipitation']
    wind_speed = weather['wind_speed']
    # weather_type = weather['weather_type']

    # assume temperature range as 0 - 50 degree celsius - (100 / (50 - 0))
    # min(max(....,0)100) - range stays between 0 - 100
    brightness = min(max(temperature * (100 / 50), 0), 100)
    # assuming 100/50 is because 100 is the max degree celsius and 50 is the max degree celsius that india can reach, can change the 50 to the max of it's own location's forcast

    if humidity > 80:
        brightness *= 0.7
    if precipitation > 0:
        brightness *= 0.5
    if wind_speed > 20:
        brightness *= 0.8

    brightness = max(0, min(brightness, 100))
    return brightness

try:
    while True:
        # fetch weather data
        weather_data = scrap_weather()

        weather = {
            'temperature' : weather_data[0],
            'weather_type': weather_data[1],
            'precipitation': weather_data[2],
            'humidity' : weather_data[3],
            'wind_speed' : weather_data[4]
        }

        brightness = cal_brightness(weather)

        led_brightness(brightness)

        time.sleep(60)  # Update every 60 seconds

except KeyboardInterrupt:
    pass


