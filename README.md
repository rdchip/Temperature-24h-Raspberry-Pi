# Temperature-24h-Raspberry-Pi
Raspberry Pi Zero project is for monitor 24h temperature using W screen 2.8-inch display. Raspberry Pi OS (32-bits) based on Debian Linux distibution, allows to install Python plus libraries. With Linux and Python installed we are able read data from DHT22 temperature sensor and plot it in the 2.8-inch display. Basically for plotting we are using Matplotlib plus a function animation, the animation add one more valeus and re-plot the graph. Each interaction takes 1 minute. The sensor also provide humidity valeu in percentage but we are just ploting temperature.

Ploting temperatures values in the display is no complicated, actually that was the easier part. Since our intention is to left running for a long time, after five days running the RAM memory start increasing finally the Raspberry Pi collapse. After debugging and research about the issue, we discover Matplotlib plotting in a loop increase the SRAM memory. 
The solution was run an small paralle bash script which run the python code for 24 hours and kill it to avoid segmentation fauls, and run the python code again. Then RAM memory never reach the 100%. The way to kill the process is saving the ID process in a file PID.txt and read it every 24 hours. Each 24 hours there are 5 seconds of no plotting. I have the project working more than 20 days with no issues.  

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

# Booting Up on the W screen display

After verifying functionality using regular monitor is time to change to 2.8" display.
Run the batch code "set_screen.sh"
$ ./set_screen.sh
The installation will reboot the system and your 2.8" display will be alive.



# Python code

# Parallel Bash code

# Desinstall 2.8" screen display

# Brightness adjustment


