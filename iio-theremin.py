#!/usr/bin/env python
from pysinewave import SineWave

# Create a sine wave, with a starting pitch of 0, and a pitch change speed of 30/second.
sinewave = SineWave(pitch = 0, pitch_per_second = 30)

# Turn the sine wave on.
sinewave.play()

while True:
    with open('/sys/bus/iio/devices/iio:device0/in_illuminance_input', 'r') as file:
        data = file.read().rstrip()
    sinewave.set_pitch(int(data))
