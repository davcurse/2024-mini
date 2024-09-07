#!/usr/bin/env python3
"""
Use analog input with photocell
"""

import time
import machine

# GP28 is ADC2
ADC2 = 28

led = machine.Pin("LED", machine.Pin.OUT)
adc = machine.ADC(ADC2)

blink_period = 0.1

# New values of max and min brightness. Print duty cycle to get normalized 0%-100% brightness 
max_bright = 500
min_bright = 52000


def clip(value: float) -> float:
    """clip number to range [0, 1]"""
    if value < 0:
        return 0
    if value > 1:
        return 1
    return value

duty_cycle = 0

while True:
    value = adc.read_u16()
    # print(value)
    print(duty_cycle * 100)
    """
    need to clip duty cycle to range [0, 1]
    this equation will give values outside the range [0, 1]
    So we use function clip()
    """

    duty_cycle = clip((value - min_bright) / (max_bright - min_bright))

    led.high()
    time.sleep(blink_period * duty_cycle)

    led.low()
    time.sleep(blink_period * (1 - duty_cycle))
