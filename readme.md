# Rack Buddy

A project for a Raspberry PI zero W based monitoring/controller device for a 10" server rack cabinet.

It's goal:
    - Measure temperature inside the cabinet
    - Control a Fan mounted in the top of the cabinet
    - Display current status on a small OLED display
    - Only display the status when presense is detected through a small PIR sensor
    - Detect door open/close state
    - Monitor UPS status
    - Publish relevant events to MQTT topic
        - Door open/close: for other systems to enable/disable displays
        - Presence detected: for other systems to enable/disable displays
        - UPS state: for other systems to initiate shutdown
    - ? Wake On Lan when power remains on?

# Hardware

* Raspberry PI Zero W
    * [PoE/ETH/USB hub hat](https://www.waveshare.com/wiki/PoE/ETH/USB_HUB_HAT)
* [AM2320](https://www.tinytronics.nl/shop/nl/sensoren/lucht/vochtigheid/am2320-thermometer-temperatuur-en-vochtigheids-sensor) I2C temperature/relative humidity sensor
* [Reed switch](https://www.tinytronics.nl/shop/nl/schakelaars/magneetschakelaars/deur-schakelaar-reed-relais-met-magneet)
* [1.3 inc OLED display 128x64px](https://www.tinytronics.nl/shop/nl/displays/oled/1.3-inch-oled-display-128*64-pixels-wit-i2c)
* [PIR Motion Sensor](https://www.tinytronics.nl/shop/nl/sensoren/beweging/ir-pyroelectrische-infrarood-pir-motion-sensor-detector-module-micro)
* [Noctua NF-F12 5V PWM case fan](https://www.alternate.nl/Noctua/NF-F12-5V-PWM-case-fan/html/product/1467326)

## AM2320
I2C address 5c

## OLED display
I2C address ?

# Software
* [Raspberry PI OS (Lite)](https://www.raspberrypi.com/software/)
* [Adafruit Blinka](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux)
* [pigpio](https://abyz.me.uk/rpi/pigpio/pigpiod.html)
    For hardware PWM, running as a service

