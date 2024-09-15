"""
Response time - single-threaded
"""

from machine import Pin
import time
import random
import json
import urequests
import network

import os

wlan = network.WLAN(network.STA_IF)
if not wlan.active() or not wlan.isconnected():
    wlan.active(True)
    wlan.connect("BU Guest (unencrypted)", "")
    while not wlan.isconnected():
        pass

N: int = 1
sample_ms = 10.0
on_ms = 500


def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(N: int, led: Pin) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


def write_json(json_filename: str, data: dict) -> None:
    """Writes data to a JSON file.

    Parameters
    ----------

    json_filename: str
        The name of the file to write to. This will overwrite any existing file.

    data: dict
        Dictionary data to write to the file.
    """

    with open(json_filename, "w") as f:
        json.dump(data, f)


def scorer(t: list[int | None]) -> None:
    # %% collate results
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")
    t_good = [x for x in t if x is not None]
    print(t_good)
    
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
        "min" : minimum,
        "max" : maximum,
        "score": score
    }

    print(data)
    urequests.post(f"https://ec463-mini-project-10f0f-default-rtdb.firebaseio.com/ {user_id} /json", data=json.dumps(data))


if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files

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
