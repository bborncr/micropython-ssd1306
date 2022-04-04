from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from time import sleep_ms

# Create I2C interface
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# Create OLED object, in this case 128 x 64 pixels
oled = SSD1306_I2C(128, 64, i2c)

# Simple text with x,y placement
oled.text("Hello", 0, 0)
oled.show()
sleep_ms(2000)
oled.text("Hello", 20, 20)
oled.show()
sleep_ms(2000)
oled.text("Hello", 40, 40)
oled.show()
sleep_ms(2000)


# Erase screen with color 0 (black) or 1 (white)
oled.fill(0)
oled.show()
sleep_ms(2000)

# Terminal mode (doesn't require oled.show())
oled.terminal("Terminal Mode")
sleep_ms(2000)
oled.terminal("Next line")
sleep_ms(2000)
oled.terminal("And another")
sleep_ms(2000)
oled.terminal("Error message")
sleep_ms(2000)
oled.terminal("Status message")
sleep_ms(2000)
oled.terminal("More than 16 characters creates multiple lines")
sleep_ms(2000)
oled.terminal("---Exactly 16---")
sleep_ms(2000)
oled.terminal("Last line")
sleep_ms(2000)

# Erase the screen again
oled.fill(0)
oled.show()

# Simple graphics
oled.rect(0,0,127,63)
oled.show()
sleep_ms(2000)
oled.fill_rect(0,0,127,63)
oled.show()
sleep_ms(2000)

# Erase the screen again
oled.fill(0)
oled.show()

# More simple graphics
oled.line(0,0,127,63)
oled.show()
sleep_ms(2000)
oled.hline(0,0,128)
oled.show()
sleep_ms(2000)
oled.vline(0,0,64)
oled.show()
sleep_ms(2000)
oled.line(0,63,127,0)
oled.show()
sleep_ms(2000)
oled.hline(0,63,128)
oled.show()
sleep_ms(2000)
oled.vline(127,0,64)
oled.show()
sleep_ms(2000)

# Erase the screen again
oled.fill(0)
oled.show()

for i in range(0,64,2):
    oled.line(0,i,127,64-i)
    oled.show()
    sleep_ms(1)
