#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# Notes
NOTE_E5  = 659
NOTE_D5  = 587
NOTE_FS4 = 370
NOTE_GS4 = 415
NOTE_CS5 = 554
NOTE_B4  = 494
NOTE_D4  = 294
NOTE_E4  = 330
NOTE_A4  = 440
NOTE_CS4 = 277

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)

nokia_ringtone = [
    (NOTE_E5, 0.08), (NOTE_D5, 0.08), (NOTE_FS4, 0.16), (NOTE_GS4, 0.16),
    (NOTE_CS5, 0.08), (NOTE_B4, 0.08), (NOTE_D4, 0.16), (NOTE_E4, 0.16),
    (NOTE_B4, 0.08), (NOTE_A4, 0.08), (NOTE_CS4, 0.16), (NOTE_E4, 0.16),
    (NOTE_A4, 0.16)
]

freq: float = 30
duration: float = 0.1  # seconds

print("Playing Nokia Ringtone! :)")

for note, duration in nokia_ringtone:
    playtone(note, duration)
    quiet()
    utime.sleep(0.01)

# Turn off the PWM
print("Finished!")
quiet()
