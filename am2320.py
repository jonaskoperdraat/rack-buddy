# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import typing

import board
import adafruit_am2320

# create the I2C shared bus
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
am = adafruit_am2320.AM2320(i2c)

delay = 3


def get_reading(lbl: str, val: typing.Callable[[], float]):
    print(lbl, ": ", end="")
    success = False
    cnt = 0
    while not success and cnt < 5:
        try:
            print(".", end="")
            print(" ", val())
            success = True
        except:
            time.sleep(delay / 10)
        finally:
            cnt += 1

    if not success:
        print("Foobar")


while True:
    get_reading("Temp", lambda: am.temperature)
    time.sleep(delay)
    get_reading("Hum ", lambda: am.relative_humidity)
    time.sleep(delay)
