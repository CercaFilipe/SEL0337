#!/bin/python

import RPi.GPIO as GPIO
import time

#definindo GPIO23 como saída
led_vermelho = 23
GPIO.setmode(GPIO.BCM)
GPIO.setmode(led_vermelho, GPIO.OUT)

while True:
        GPIO.output(led_vermelho, GPIO.HIGH)
        print("LED ACESO")
        time.sleep(1)
        print("LED APAGADO")
        GPIO.output(led_vermelho, GPIO.LOW)
        time.sleep(1)

