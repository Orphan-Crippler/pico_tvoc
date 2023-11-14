
# Raspberry Pi Pico Total Volatile Organic Compound (TVOC) &amp; Equivalent Carbon Dioxide (eCo2) Sensor

![PXL_20231111_053156907 MP](https://github.com/Orphan-Crippler/pico_tvoc/assets/6201093/53339fda-f87e-4628-ba14-df3d1e3b5163)

This was a quick thing I threw together to measure Total Volatile Organic Compounds in the air where I 3D Print. I have included data sheets for the sensor and the raspberry Pi, the oled screen is just a cheap chinese I2C screen I picked up on Amazon. So I could not find a data sheet for it. Well let's get to it, shall we.

## Parts List

+ Raspberry Pi Pico (Pico W) will also work with no code changes. https://www.adafruit.com/pico?src=raspberrypi
+ ~~Adafruit CCS811 Sensor~~ This was recently discontinued and replaced by the Adafruit SGP30 https://www.adafruit.com/product/3709
+ 128x64 I2C OLED LCD https://www.amazon.com/gp/product/B0B7RP2CVT/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1
+ NeoPixel 8 Stick https://www.adafruit.com/product/1426

So I originally made this project many years ago with the Adafruit CCS811 sensor. Well when I was gathering links for the parts I found out that this sensor breakout has been discontinued by the manufacturer. Luckily there is an upgraded replacement the SGP30 sensor that measures the same things and has a couple new features. I will leave the CCS811 code and schematics in a folder in case anyone still has one of these laying around. I was finally able to find a working SGP30 driver for Micro Python and have updated the folder and main.py file.

## Install MicroPython and Thonny

This link has all the information for isntalling Thonny and MicroPython on the Raspberry Pi Pico.
+ https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/0

## Wiring up the sensor, screen, and LED's
Follow the schematic for the sensor you are using. The schematics are in their respective folders.

## Copy files to Pico using Thonny
Open the three python files in Thonny. These are downloaded from this repository for the sensor you plan on using. There are multiple ways to add these files to your Pico from Thonny. You must put all three files on the Pico. Once you have then loaded on your Pico you can run the main.py file to test it out. If everything is working you can unplug the Pico from the PC. Your sensor is ready to get to work. At this point you do not need to plug the Pico into a PC and may power it however you please.

## Note on Sensor Placement
To get truly accurate readings, the sensor must be on your person when measuring. If it is across the room from you it may not accurately reflect TVOC levels where you are in the room. As a precaution you should always have sufficient ventilation in any area you are using a 3D printer.
