"""
Response time - single-threaded
"""

from machine import Pin
import time
import random
import json
import urequests
import network

wlan = network.WLAN(network.STA_IF)
if not wlan.active() or not wlan.isconnected():
    wlan.active(True)
    wlan.connect("BU Guest (unencrypted)", "")
    while not wlan.isconnected(): 
        pass

N: int = 10
sample_ms = 10.0
on_ms = 500

def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min."""
    return random.uniform(tmin, tmax)


def blinker(N: int, led: Pin) -> None:
    """Let user know game started or is over.
    
    Args:
        N: number of rounds
        led: GPIO pin for LED
    """
    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


def scorer(t: list[int | None]) -> None:
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")
    t_good = [x for x in t if x is not None]
    
    for count, time in enumerate(t_good):
        print(f"Trial {count}: {time} ms")
    
    if not t_good:
        average =  0
        minimum = 0
        maximum = 0
        score = 0
    else:
        average = sum(t_good) / len(t_good)
        minimum = min(t_good)
        maximum = max(t_good)
        score = len(t_good)/len(t)

    data = {
        "avg_ms" : average,
        "min_ms" : minimum,
        "max_ms" : maximum,
        "score": score
    }

    print(data)
    urequests.post("https://ec463-mini-project-10f0f-default-rtdb.firebaseio.com/data.json", data=json.dumps(data))


if __name__ == "__main__":

    led = Pin("LED", Pin.OUT)
    button = Pin(12, Pin.IN, Pin.PULL_UP)

    t: list[int | None] = []

    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                break
        t.append(t0)

        led.low()

    blinker(5, led)

    scorer(t)

