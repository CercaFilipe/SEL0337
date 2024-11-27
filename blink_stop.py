#!/bin/python

import RPi.GPIO as GPIO
import time

led_pin=24
led_vermelho=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(led_vermelho, GPIO.OUT)

try:
        while True:
                GPIO.output(led_vermelho, GPIO.LOW)
                GPIO.output(led_pin, GPIO.HIGH)
                print("STOP => VERDE ATIVO")
                time.sleep(1)

except KeyboardInterrupt:
        print("Para")

finally:
        GPIO.cleanup()