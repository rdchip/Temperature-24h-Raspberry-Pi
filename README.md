Temperature 24h Raspberry Pi 
=======
Raspberry Pi Zero project is for monitor 24h temperature using W screen 2.8-inch display. Raspberry Pi OS (32-bits) based on Debian Linux distibution, allows to install Python plus libraries. With Linux and Python installed we are able read data from DHT22 temperature sensor and plot it in the 2.8-inch display. Basically for plotting we are using Matplotlib plus a function animation, the animation add one more valeus and re-plot the graph. Each interaction takes 1 minute. The sensor also provide humidity valeu in percentage but we are just ploting temperature.

Ploting temperatures values in the display is no complicated, actually that was the easier part. Since our intention is to left running for a long time, after five days running the RAM memory start increasing finally the Raspberry Pi collapse. After debugging and research about the issue, we discover Matplotlib plotting in a loop increase the SRAM memory. 
The solution was run an small paralle bash script which run the python code for 24 hours and kill it to avoid segmentation fauls, and run the python code again. Then RAM memory never reach the 100%. The way to kill the process is saving the ID process in a file PID.txt and read it every 24 hours. Each 24 hours there are 5 seconds of no plotting. I have the project working more than 20 days with no issues.  

This project is implemented for monitoring 24 hours in Python.

<img src="picture/IMG_0604.jpg" width=480>       <img src="picture/IMG_0350.jpg" width=480>

# Requirements

Raspberry Pi Zero --------------- W Screen 2.8-inch Display -------------- DHT22 Temperature Sensor 

<img src="picture/IMG_0325 (2).jpg" width=172>  <img src="picture/iUniker.jpg" width=295> <img src="picture/DHT22-sensorT.jpg" width=300>


https://www.amazon.com/gp/product/B071L2ZQZX/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1

Raspberry Pi Zero W Screen iUniker 2.8-inch 60+ fps 640x480
https://www.amazon.com/gp/product/B07H8ZY89H/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1

DHT22 / AM2302 Digital Humidity and Temperature Sensor Module
https://www.amazon.com/gp/product/B073F472JL/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1

MicroSD memory

# Relevant Information

Raspberry Pi Zero GPIO pin distribution

<img src="picture/Pi ports.png" width=512>    <img src="picture/pin_map.png" width=448>

W Screen iUniker 2.8" GPIO pin distribution, Temperature Sensor pin distribution

<img src="picture/screen_map.png" width=367>   <img src="picture/sensor_map.png" width=300>

# Instructions
- Create Raspberry Pi Linux image
- Sensor temperature connection and 2.8" display 
- Power up Raspberry with Linux
  - Install Python and libraries
- Test python project code
- Install W screen Display 2.8-inch
- Learn un-install LCD screen
- Reduce the brightness 
- Parallel bash code 

# Raspberry Pi Linux Image

Basically, the Raspberry Pi needs an Operating System (OS) in order to do any job. Then the microSD memory will store the OS, in this case is Raspbian.
In this section we will install the Raspbian in the microSD memory. 
Just go to www.raspberrypi.com/software/ and download "Raspberry Pi Imager v1.6"

Choose the right version:
-  Download for Windows
-  Download for macOS
-  Download for Ubuntu for x86

<img src="picture/imager.png" width=400>

After download and install "Raspberry Pi Imager" open it and click in "CHOOSE OS", since is the first time, select "Raspberry Pi OS (32-bits)".
Next, select the storage: click in "CHOOSE STORAGE" and select your microSD memory. Finally click in "WRITE" to create the boot card. At the end, you will see something like this:

<img src="picture/imager2.png" width=400>

Now the microSD memory is ready to place in the Raspberry Pi Zero.   

# Sensor temperature connection and 2.8"Display

The table shows the pin assigment to connect the sensor tmeperature and the Raspberry Pi Zero. Solder first the 2.8" display with the Raspberry Pi Zero and later solder the cables of the sensor. If you are planning to use the Raspberry for other project also, I recomend use 2x20 Pin Female Header as extension, so you can remove the display easily.  

<img src="picture/table_sensor.png" width=200>
<img src="picture/zero_plus_display.png" width=400>
<img src="picture/connection.png" width=400>

At this point, all hardware is connected and the operating system (Linux) is ready but the 2.8" display won't wake-up because there is not drivers installed. Let's power up and install Python, libraries and drivers.

# Power up Raspberry Pi Zero

Connect the mini HDMI cable to the monitor, also keyboard and mouse using usb hub, place the microSD memory and power up. Linux will prompt in your monitor. 
Since is the first boot, you need to follow the guide to setup your language, local time, and all things. The most important is the wifi connection because you need to update the OS. If for some reason you get problems with the wifi connection, just reboot several times (maybe 5 times) after you get the internet connection, and update Linux.

<img src="picture/welcome.png" width=950>

Open the terminal and run the command for update:
````sh
$ sudo apt update
````
Later
````sh
$ sudo apt full-upgrade
````
It will take longer, maybe 1 hour to finish.

Now you can install Python and all libraries from the terminal. 

- Install Python 2.7  (Python 2.7 should be already installed, type python in the terminal and you will see). Otherwise type:
````sh
$ sudo apt install python2.7
````
Install parallel
````sh
$ sudo apt install parallel
````
Install Libraries:

- Adafruit_DHT
````sh
$ sudo pip install Adafruit_DHT
````
- import psutil
````sh
$ sudo pip install psutil
````
- import numpy as np
````sh
$ sudo pip install numpy
````
- import matplotlib
````sh
$ sudo apt install python-matplotlib
````

- install screensaver (in case you need to disable the screensaver)
````sh
$ sudo apt install xscreensaver
````

Increasing the Swap File on a Raspberry Pi

https://pimylifeup.com/raspberry-pi-swap-file/

After all library installed, is time to see the temperature graph in the big monitor.

Download the folder MZDPI and all files from codes section. Keep the same file organization. Create a folder colled Raspberry and place all inside. You will have somthing like this:

<img src="picture/file_organization.png" width=950>

If all is ok until this point we can run the temperature plot, do the next steps:

change directory:
````sh
$ cd Raspberry
````
run the command:
````sh
$ sudo bash temp.sh
````

The plot will apears like this:

<img src="picture/temperature_plot.png" width=950>


# Booting Up on the W 2.8" screen display

After verifying functionality using regular monitor is time to change to 2.8" display.
From the terminal, go to the Raspberry folder and run the batch code "set_screen.sh"
````sh
$ ./set_screen.sh
````
The installation will reboot the system and your 2.8" display will be alive.
Now is time to run the temperature code.
From the terminal run "temp.sh"
````sh
$ ./temp.sh
````

# Python code

# Parallel Bash code

<img src="picture/parallel.png" width=300>

# Uninstall 2.8" screen display

# Brightness adjustment


