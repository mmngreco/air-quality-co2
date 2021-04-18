#!/bin/bash
export AMPY_PORT=/dev/ttyUSB0 # or your port to the ESP
ampy put sensor_s8.py
ampy run -n sensor_s8.py
