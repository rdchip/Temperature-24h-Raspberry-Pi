# Temperature-24h-Raspberry-Pi
Raspberry Pi Zero project is for monitor 24h temperature using W screen 2.8-inch display. Raspberry Pi OS (32-bits) based on Debian Linux distibution, allows to install Python plus libraries. With Linux and Python installed we are able read data from DHT22 temperature sensor and plot it in the 2.8-inch display. Basically for plotting we are using Matplotlib plus a function animation, the animation add one more valeus and re-plot the graph. Each interaction takes 1 minute. The sensor also provide humidity valeu in percentage but we are just ploting temperature.

Ploting temperatures values in the display is no complicated, actually that was the easier part. Since our intention is to left running for a long time, after five days running the RAM memory start increasing until Raspberry Pi collapse.

This project is implemented for monitoring 24 hours in Python.

<img src="picture/IMG_0604.jpg" width=300>       <img src="picture/IMG_0350.jpg" width=300>

# Requirements

Raspberry Pi Zero

<img src="picture/IMG_0325 (2).jpg" width=172>  <img src="picture/iUniker.jpg" width=295> <img src="picture/DHT22-sensorT.jpg" width=300>


https://www.amazon.com/gp/product/B071L2ZQZX/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1

Raspberry Pi Zero W Screen iUniker 2.8-inch 60+ fps 640x480
https://www.amazon.com/gp/product/B07H8ZY89H/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1

DHT22 / AM2302 Digital Humidity and Temperature Sensor Module
https://www.amazon.com/gp/product/B073F472JL/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1

MicroSD memory 

# Instructions
- Create Raspberry Pi Linux image 
- Power up Raspberry with Linux
- Install Python
- Install libraries for python
- Sensor temperature connection
- Test python project code
- Install LCD screen
- Learn un-install LCD screen
- Reduce the brightness 
- Parallel bash code 

# Raspberry Pi Linux Image

Raspberry Pi Zero GPIO pin distribution

<img src="picture/Pi ports.png" width=512>    <img src="picture/pin_map.png" width=448>

W Screen iUniker 2.8" GPIO pin distribution, Temperature Sensor pin distribution

<img src="picture/screen_map.png" width=367>   <img src="picture/sensor_map.png" width=300>




# Python code

# Parallel Bash code
