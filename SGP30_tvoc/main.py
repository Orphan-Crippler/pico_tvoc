from machine import Pin, I2C
import ssd1306, ccs811, neopixel, utime

# setup NeoPixel
np = neopixel.NeoPixel(machine.Pin(0), 8)
np2 = neopixel.NeoPixel(machine.Pin(2), 8)

# setup I2C for display
i2c0 = I2C(0, sda=Pin(16), scl=Pin(17))
utime.sleep_ms(100)
display = ssd1306.SSD1306_I2C(128, 64, i2c0)

# setup I2C for sensor
i2c1 = I2C(1, sda=Pin(18), scl=Pin(19))
voc = ccs811.CCS811(i2c1)
voc.setup()

# Splash/Loading Screen & LED Test. Not neccesary but looks nice.
def splash():
    display.text('Air Quality', 0, 0)
    display.text('        Monitor', 0, 8)
    display.text('    Loading', 0, 16)
    display.show()

    range = [0,1,2,3,4,5,6,7]
    for i in range:
        np[i] = (255, 0, 0)
        np2[i] = (255, 0, 0)
        np.write()
        np2.write()
        display.text('%' * i, 0, 24)
        display.show()
        utime.sleep_ms(250)
    
    range = [7,6,5,4,3,2,1,0]
    prog = 8
    for i in range:
        np[i] = (0, 255, 0)
        np2[i] = (0, 255, 0)
        np.write()
        np2.write()
        display.text('%' * prog, 0, 24)
        display.show()
        prog += 1
        utime.sleep_ms(250)

    range = [0,1,2,3,4,5,6,7]
    prog2 = 16
    for i in range:
        np[i] = (0, 0, 255)
        np2[i] = (0, 0, 255)
        np.write()
        np2.write()
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
    global r
    if r[1] <= 220:
        range = [0,1,2,3,4,5,6,7]
        for i in range:
            np[i] = (0, 255, 0)
            np.write()
    elif r[1] >= 221 <= 660:
        line1 = 'Ventilation!!'
        range = [0,1,2,3,4,5,6,7]
        for i in range:
            np[i] = (255, 25, 0)
            np.write()
        utime.sleep(2)
    if r[1] >= 661:
        line1 = '!!!!DANGER!!!!'
        range = [0,1,2,3,4,5,6,7]
        for i in range:
            np[i] = (255, 0, 0)
            np.write()
        utime.sleep(2)
        
def chkCo2():
    global line2
    global r
    if r[0] <= 600:
        range = [0,1,2,3,4,5,6,7]
        for i in range:
            np2[i] = (0, 255, 0)
            np2.write()
    elif r[0] >= 601 <= 1000:
        range = [0,1,2,3,4,5,6,7]
        for i in range:
            np2[i] = (255, 168, 0)
            np2.write()
    elif r[0] >= 1001 <= 1500:
        line2 = 'Ventilation!!'
        range = [0,1,2,3,4,5,6,7]
        for i in range:
            np2[i] = (255, 25, 0)
            np2.write()
        utime.sleep(2)
    if r[0] >= 1501:
        line2 = 'Co2 EVACUATE!!'
        range = [0,1,2,3,4,5,6,7]
        for i in range:
            np2[i] = (255, 0, 0)
            np2.write()
        utime.sleep(2)

splash()
# Loop
while True:
    global line1
    global line2
    line1 = ''
    line2 = ''
    
    if voc.data_available():
        global r
        r = voc.read_algorithm_results()
         
        chkCo2()
        
        chkTVOC()
        
        display.fill(0)
        display.show()
        display.text('Air Quality', 0, 0)
        display.text('        Monitor', 0, 8)
        display.text('eCo2:' + str(r[0]) + 'ppm', 0, 16)
        display.text(line2, 0, 24)
        display.text('TVOC:' + str(r[1]) + 'ppb', 0, 48)
        display.text(line1, 0, 56)
        display.show()
        utime.sleep(1)
    else:
        display.fill(0)
        display.text('CCS811 ERROR', 0, 0)
        display.show()
