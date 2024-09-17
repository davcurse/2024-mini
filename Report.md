### Exercise 1

Max brightness = 500\
Min brightness = 52000

Commented out `print(value)`\
Added `print(duty_cycle * 100)`

### Exercise 2

Modified code and wired up PWM speaker to play Nokia theme song.

Notes added corresponding to their frequency:
```
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
```

Nokia Ringtone Frequency/Notes:
```
nokia_ringtone = [
    (NOTE_E5, 0.08), (NOTE_D5, 0.08), (NOTE_FS4, 0.16), (NOTE_GS4, 0.16),
    (NOTE_CS5, 0.08), (NOTE_B4, 0.08), (NOTE_D4, 0.16), (NOTE_E4, 0.16),
    (NOTE_B4, 0.08), (NOTE_A4, 0.08), (NOTE_CS4, 0.16), (NOTE_E4, 0.16),
    (NOTE_A4, 0.16)
]
```

### Exercise 3

Completed button game.

Connected raspberry pi pico to the internet via network library:

```
wlan = network.WLAN(network.STA_IF)
if not wlan.active() or not wlan.isconnected():
    wlan.active(True)
    wlan.connect("BU Guest (unencrypted)", "")
    while not wlan.isconnected(): 
        pass
```

Sent button game results to firebase cloud via urequests library:

```
urequests.post("https://ec463-mini-project-10f0f-default-rtdb.firebaseio.com/data.json", data=json.dumps(data))
```

Screenshot of firebase cloud with data is seen in top level readme file.
