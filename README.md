
# Raspberry Pi Pico W Total Volatile Organic Compound (TVOC) &amp; Equivalent Carbon Dioxide (eCo2) Sensor

![PXL_20231111_053156907 MP](https://github.com/Orphan-Crippler/pico_tvoc/assets/6201093/53339fda-f87e-4628-ba14-df3d1e3b5163)

This was a quick thing I threw together to measure Total Volatile Organic Compounds in the air where I 3D Print. I have included data sheets for the sensor and the raspberry Pi, the oled screen is just a cheap chinese I2C screen I picked up on Amazon for cheap. So I could not find a data sheet for it. Well let's get to it, shall we.

## Parts List

+ Raspberry Pi Pico (Pico W) will also work with no code changes.
+ ~~Adafruit CCS811 Sensor~~ This was recently discontinued and replaced by the Adafruit SGP30 https://www.adafruit.com/product/3709
+ 128x64 I2C OLED LCD https://www.amazon.com/gp/product/B0B7RP2CVT/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1
+ NeoPixel 8 Stick https://www.adafruit.com/product/1426

So I originally made this project many years ago with the Adafruit CCS811 sensor. Well when I was gathering links for the parts I found out that this sensor breakout has been discontinued by the manufacturer. Luckily there is an upgraded replacement the SGP30 sensor measures the same things and has a few extra features. I will leave CCS811 code and schematics in a folder in case anyone still has one of these lying around.
