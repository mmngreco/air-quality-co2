# Air quality

WIP Project

https://medium.com/@rubfi/measuring-co2-with-esp8266-and-micropython-41a599e927a6
https://micropython.org/download/esp8266/
https://developer.ridgerun.com/wiki/index.php/Setting_up_Picocom_-_Ubuntu

```bash
conda create -n co2 python=3.8
conda activate co2
pip install esptool
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 esp8266-20210202-v1.14.bin
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 esp8266-20200911-v1.13.bin
```

```bash
#!/bin/bash
export AMPY_PORT=/dev/ttyUSB0 # or your port to the ESP
ampy put sensor_s8.py --port /dev/ttyUSB0
ampy ls
ampy run sensor_s8.py
ampy put helloworld.py
ampy run helloworld.py
ampy rm helloworld.py
ampy rm sensor_s8.py
```

```bash
#!/bin/bash
picocom -b 115200 -r -l $AMPY_PORT
picocom /dev/ttyUSB0 -b115200
picocom /dev/ttyACM2
```
