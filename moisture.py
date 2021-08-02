import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI
import time

# Programme for reading and interpreting data from the
# HW-390 Capacitive Moisture Sensor v2.0.
# Import SPI library (for hardware SPI) and MCP3008 library.
# Software SPI configueration:
CLK = 18
MISO = 23
MOSI = 24
CS = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# MCP3008 Channel.
chan = 0

# Opening message.
print('Reading HW-390 values, press Ctrl-C to quit...')

# Main program loop.
while True:
    # Get the reading from the specified channel (chan) of the ADC.
    data = mcp.read_adc(chan)
    # Print the reading.
    print('Reading: >4'.format(data))
    # Wait for half a second before next reading.
    time.sleep(0.5)
