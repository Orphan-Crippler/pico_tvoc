from machine import Pin, I2C
import ssd1306, adafruit_sgp30, neopixel, utime

# setup NeoPixel
np = neopixel.NeoPixel(machine.Pin(0), 8)

# setup I2C for display
i2c0 = I2C(0, sda=Pin(16), scl=Pin(17))
utime.sleep_ms(100)
display = ssd1306.SSD1306_I2C(128, 64, i2c0)

# setup I2C for sensor
i2c1 = I2C(1, scl=Pin(19), sda=Pin(18), freq=100000)
sgp = adafruit_sgp30.Adafruit_SGP30(i2c1)


# Splash/Loading Screen & LED Test. Not neccesary but looks nice.
def splash():
    display.text('Air Quality', 0, 0)
    display.text('        Monitor', 0, 8)
    display.text('    Loading', 0, 16)
    display.show()

    range = [0,1,2,3,4,5,6,7]
    for i in range:
        np[i] = (255, 0, 0)
        np.write()
        display.text('%' * i, 0, 24)
        display.show()
        utime.sleep_ms(250)
    
    range = [7,6,5,4,3,2,1,0]
    prog = 8
    for i in range:
        np[i] = (0, 255, 0)
        np.write()
        display.text('%' * prog, 0, 24)
        display.show()
        prog += 1
        utime.sleep_ms(250)

    range = [0,1,2,3,4,5,6,7]
    prog2 = 16
    for i in range:
        np[i] = (0, 0, 255)
        np.write()
        display.fill(0)
        display.show()
        display.text('Air Quality', 0, 0)
        display.text('        Monitor', 0, 8)
        display.text('    Loading', 0, 16)
        display.text('%' * prog2, 0, 24)
        display.show()
        prog2 -= 2
        utime.sleep_ms(250)

"""
Co2 ppm
400~600 Excellent
700~800 Good
900~1000 Fair
1100~1500 Fair (Ventilation Recommended)
1600~2100 BAD (Ventilation REQUIRED)

TVOC ppb
0~220 Good
221~660 Moderate (Ventilation Recommended)
661~1430 High (Ventilation REQUIRED)
"""
def chkTVOC():
    global line1
    if tvoc <= 220:
        range = [0,1,2,3,4,5,6,7]
        for i in range:
            np[i] = (0, 255, 0)
            np.write()
    elif tvoc >= 221 <= 660:
        line1 = 'TVOC Ventilation!!'
        range = [0,1,2,3,4,5,6,7]
        for i in range:
            np[i] = (255, 25, 0)
            np.write()
        utime.sleep(2)
    if tvoc >= 661:
        line1 = 'TVOC EVACUATE!!'
        range = [0,1,2,3,4,5,6,7]
        for i in range:
            np[i] = (255, 0, 0)
            np.write()
        utime.sleep(2)
        
def chkCo2():
    global line2
    if co2eq <= 600:
        utime.sleep(2)
    elif co2eq >= 601 <= 1000:
        utime.sleep(2)
    elif co2eq >= 1001 <= 1500:
        line2 = 'Co2 Ventilation!!'
        utime.sleep(2)
    if co2eq >= 1501:
        line2 = 'Co2 EVACUATE!!'
        utime.sleep(2)

splash()
# Loop
while True:
    co2eq, tvoc = sgp.iaq_measure()
    global line1
    global line2
    line1 = ''
    line2 = ''
         
    chkCo2()
        
    chkTVOC()
        
    display.fill(0)
    display.show()
    display.text('Air Quality', 0, 0)
    display.text('        Monitor', 0, 8)
    display.text('eCo2:' + str(co2eq) + 'ppm', 0, 16)
    display.text(line2, 0, 24)
    display.text('TVOC:' + str(tvoc) + 'ppb', 0, 48)
    display.text(line1, 0, 56)
    display.show()
    utime.sleep(1)
    