Temperature 24h Raspberry Pi 
=======
Raspberry Pi Zero project is for monitoring 24h temperature with screen 2.8-inch display. Raspberry Pi OS (32-bits) based on Debian Linux distibution, allows to install Python plus libraries. Using Linux and Python we are able read data from DHT22 temperature sensor and plot it in the 2.8-inch display. Basically for plotting we are using Matplotlib and update the plot every 60 seconds. The sensor also provide humidity values in percentage but we are just ploting temperature.

Ploting temperatures values in the display is no complicated, actually that was the easier part. Since our intention is to keep running for a long time (infinite loop), we discover after five days running, the RAM start increasing and finally the Raspberry Pi collapse (segmentation fault). After debugging and research about the issue, we discovered Matplotlib is causing this issue. 
The solution is run a paralle bash script which run the python code for 24 hours and kill it to avoid segmentation fauls, and run the python code again. Then RAM memory never reach the 100%. Then, we save the python code ID process in PID.txt file and read it every 24 hours. So every 24 hours there are 30 seconds with no plot. I have the project working more than 20 days with no issues.  


<img src="picture/IMG_0825.jpg" width=480>       <img src="picture/IMG_0350.jpg" width=480>

# Requirements

Raspberry Pi Zero --------------- W Screen 2.8-inch Display -------------- DHT22 Temperature Sensor 

<img src="picture/IMG_0325 (2).jpg" width=172>  <img src="picture/iUniker.jpg" width=295> <img src="picture/DHT22-sensorT.jpg" width=300>


https://www.amazon.com/gp/product/B071L2ZQZX/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1

Raspberry Pi Zero W Screen iUniker 3.5 inch 60+ fps 640x480 (2.8" display is no longer available, 3.5" works fine)
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

Basically, the Raspberry Pi needs an Operating System (OS) to work. Then, we use microSD memory to store the OS. In this case Raspberry use Linux Raspbian.
In this section we will install the Raspbian in the microSD memory of 32GbB. 
Just go to www.raspberrypi.com/software/ and download "Raspberry Pi Imager v1.6"

Choose the right version:
-  Download for Windows
-  Download for macOS
-  Download for Ubuntu for x86

<img src="picture/imager.png" width=400>

After download and install "Raspberry Pi Imager" open it and click in "CHOOSE OS", since is the first time, I recomend install the full version (Python3 and libraries included). Then, select "Raspberry Pi OS FULL (32-bits)" which is under "Raspberry Pi OS (others)".

<img src="picture/OS_full.png" width=400>

Next, select the storage: click in "CHOOSE STORAGE" and select your microSD memory. Finally, click in "WRITE" to create the boot card. At the end, you will see something like this:

<img src="picture/imager2.png" width=400>

Now, the microSD memory is ready to place in the Raspberry Pi Zero.   

# Sensor temperature connection and 2.8"Display

The table shows the pin assigment to connect the sensor temperature and the Raspberry Pi Zero. Solder first the 2.8" display with the Raspberry Pi Zero and later solder the cables of the sensor. If you are planning to use the Raspberry for other project also, I recomend use 2x20 Pin Female Header as extension, so you can remove the display easily.  

<img src="picture/table_sensor.png" width=200>
<img src="picture/zero_plus_display.png" width=400>
<img src="picture/connection.png" width=400>

At this point, all hardware is connected and the operating system (Linux) is ready but the 2.8" display won't wake-up because there is not drivers installed. Let's power up and install Python, libraries and drivers.

# Power up Raspberry Pi Zero

Connect the mini HDMI cable to your monitor, I recomend connect your keyboard and mouse using usb hub. Now, place the microSD memory and power up. Linux will prompt in your monitor. 
Since is the first time booting, you need to follow the instructions to setup your language, local time, and other things. At this point, the wifi connection is important, because you need to update the OS and install libraries/drivers. If for some reason you are facing problems with the wifi connection, maybe is the wifi chip is hot. Just let it coolling down.

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

Now you can install libraries for Python3 in the terminal. 

- Python3 should be already installed, type python3 in the terminal and you will see.

Install parallel
````sh
$ sudo apt install parallel
````
Install temperature sensor Libraries:

- Adafruit_DHT
````sh
$ sudo pip3 install Adafruit_DHT
````

Just in case there are no installed use the following commands (all these 3 libraries should be installed using full OS).

- Install psutil
````sh
$ sudo pip3 install psutil
````
- Install numpy as np
````sh
$ sudo pip3 install numpy
````
- Install matplotlib
````sh
$ sudo apt install python3-matplotlib
````

- Install screensaver (in case you need to disable the screensaver)
````sh
$ sudo apt install xscreensaver
````

- Install virtual keyboard (in case you need it)
````sh
$ sudo apt install matchbox-keyboard
````

keyboard will be in accessories

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

The plot will appears like this:

<img src="picture/temperature_plot.png" width=950>



# Booting Up on the W 2.8" screen display

After verifying functionality using regular monitor is time to change to 2.8" display. When you switch the monitor, the resolution change and is not easy to deal with the terminal. Before switch the monitor I recomend change the font size of the Terminal to 18.

In the terminal go to menu Edit-->Preference-->Style, click in the font, on the bottom, change the size to 18.


<img src="picture/font_size.png" width=950>

When you install the 2.8"display the system will reboot and your big monitor will no longer available. If you want the big monitor back again, you need to uninstall the 2.8"display. Since the project is plot the temperature all the time, all is ok.


From the terminal, go to the Raspberry folder and run the batch code "set_screen.sh" to install the 2.8"display.
````sh
$ sudo bash set_screen.sh
````
The installation will reboot the system and your 2.8" display will be alive.
Now is time to run the temperature code.
From the terminal run "temp.sh"
````sh
$ sudo bash temp.sh
````

# Python code

# Parallel Bash code

<img src="picture/parallel.png" width=300>

# Uninstall 2.8" screen display

In case you need to uninstall the 2.8"display, just go to the terminal and run this:
````sh
$ sudo bash off_screen.sh
````
The system will reboot and your big monitor will back if it is connected.

# Brightness adjustment

In oreder to reduce the brightness of the 2.8" display, there are two pads that need to be in short circuit, solder this pins and run the bash code:
````sh
$ sudo bash tft.sh
````
You can modify the brightness from 0 to 100%, just open the file and edit the value, now is set at 80%
````sh
gpio -g mode 18 pwm
gpio pwmc 1000
gpio -g pwm 18 80
````

<img src="picture/display_pwm.png" width=300>
