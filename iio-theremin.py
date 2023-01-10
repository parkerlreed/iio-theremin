#!/usr/bin/env python
import time
import sys
import signal
from pysinewave import SineWave

signal.signal(signal.SIGINT, signal.default_int_handler)

# Create a sine wave, with a starting pitch of 12, and a pitch change speed of 10/second.
sinewave = SineWave(pitch = 0, pitch_per_second = int(sys.argv[1]))

# Turn the sine wave on.
sinewave.play()

while True:
    try:
        file = open('/sys/bus/iio/devices/iio:device0/in_illuminance_input', 'r')
        data = file.read().rstrip()
        sinewave.set_pitch(int(data))
    except KeyboardInterrupt:
        sinewave.stop()
        file.close()
        sys.exit()
