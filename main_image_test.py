from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from time import sleep_ms

# Create I2C interface
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# Create OLED object, in this case 128 x 64 pixels
oled = SSD1306_I2C(128, 64, i2c)

oled.text("Hello", 0, 0)
oled.show()
