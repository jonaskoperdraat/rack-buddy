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
            print(" {:.1f}".format(val()))
            success = True
        except:
            time.sleep(delay / 10)
        finally:
            cnt += 1

    if not success:
        print("Foobar")


def get_system_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        t = float(f.read())
        return t / 1000


while True:
    get_reading("PI temp:    ", lambda: get_system_temp())
    time.sleep(delay)
    get_reading("AM2320 temp:", lambda: am.temperature)
    time.sleep(delay)
    get_reading("AM2320 hum: ", lambda: am.relative_humidity)
