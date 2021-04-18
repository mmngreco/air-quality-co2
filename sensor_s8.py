from machine import UART, Pin
rx_pin = Pin(21, Pin.IN)
tx_pin = Pin(22, Pin.OUT)
help(Pin)
uart = UART(1, baudrate=9600, bits=8, parity=None, stop=1, tx=tx_pin, rx=rx_pin)
bid = uart.write(b'\xff\x01\x86\x00\x00\x00\x00\x00\x79')
buf = uart.read(bid)
co2 = buf[2] * 256 + buf[3]
print('co2 = %.2f' % co2)
