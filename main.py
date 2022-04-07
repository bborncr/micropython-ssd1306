from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from time import sleep_ms
import framebuf # only for image test

# Create I2C interface
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# Create OLED object, in this case 128 x 64 pixels
oled = SSD1306_I2C(128, 64, i2c)

# Image test
# Create .pbm files with GIMP
# Make the background white with image in black
# Create a framebuffer and use blit to add to display
with open('logo.pbm', 'rb') as f:
    f.readline() # Magic number
    f.readline() # Creator comment
    width, height = f.readline().decode().split(" ") # Dimensions
    data = bytearray(f.read())
    fbuf = framebuf.FrameBuffer(data, int(width), int(height), framebuf.MONO_HLSB)
    
oled.blit(fbuf, 5, 0)
oled.show()

oled.text("Value: ",5,20)
for i in range(128):
    oled.fill_rect(5,35,i,10)
    oled.text(str(i),5+(7*7),20)
    oled.show()
    oled.text(str(i),5+(7*7),20,0) # paint former text black before looping

for i in reversed(range(128)):
    oled.fill_rect(5,35,i,10)
    oled.text(str(i),5+(7*7),20)
    oled.show()
    oled.text(str(i),5+(7*7),20,0) # paint former text black before looping
    oled.fill_rect(5,35,i,10,0) # paint former rectangle black before looping

sleep_ms(2000)
oled.fill(0)
oled.show()

# Simple text with x,y placement
oled.text("Hello", 0, 0)
oled.show()
sleep_ms(1000)
oled.text("Hello", 20, 20)
oled.show()
sleep_ms(1000)
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
sleep_ms(1000)
oled.terminal("And another")
sleep_ms(1000)
oled.terminal("Error message")
sleep_ms(1000)
oled.terminal("Status message")
sleep_ms(1000)
oled.terminal("More than 16 characters creates multiple lines")
sleep_ms(1000)
oled.terminal("---Exactly 16---")
sleep_ms(1000)
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
sleep_ms(1000)
oled.hline(0,0,128)
oled.show()
sleep_ms(1000)
oled.vline(0,0,64)
oled.show()
sleep_ms(1000)
oled.line(0,63,127,0)
oled.show()
sleep_ms(1000)
oled.hline(0,63,128)
oled.show()
sleep_ms(1000)
oled.vline(127,0,64)
oled.show()
sleep_ms(2000)

oled.fill(0)
oled.show()

for i in range(0,64,2):
    oled.line(0,i,127,64-i)
    oled.show()
