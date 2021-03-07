# python-IoTSensor

How to build a LoPy4 temperature sensor

Created by Robin (rh222sa), student at “Introduction to Applied Internet of Things” at Linnaeus University.
This is a tutorial on how to build and program an IoT device to enable it to measure temperature and send temperature data to a cloud platform for viewing and storage. This project takes approximately 2-4 hours to complete and does not require prior experience in programming or electronics.

Objective

The purpose of this device is, in general, to measure the temperature of the environment. In particular, I have chosen to create this device to gain some insight into the temperature differences at various locations in my apartment. There is some debate among the room mates as to who deserves to have the one functional radiator in his room. This device may settle the dispute in an empirical, objective manner.

Material

All of this material was purchased at an online tech store called Electrokit. The following components can be purchased for a total of well under 1,000 SEK. The components used in this project are as follows:

Pycom LoPy4: a development board that executes MicroPython code.
Pycom Expansion Board v3.1: a board that creates wiring possibilities between the sensor inputs and the LoPy4, as well as providing USB connectivity.
LoRa/SigFox Antenna: provides a WiFi or LoRa/SigFox connection between the LoPy4 and some wireless external source.
Breadboard: a circuit board enabling simple wiring for IoT prototypes.
MCP9700 Temperature Sensor: a very small component for measuring the temperature of its environment. It has three pins: the left one provides the power, the middle one provides the signal, and the right one provides the ground.
USB cord: a Micro USB cable.
Circuit wires: simple jumping wire cables.
Other components were included in the bundle purchased from Electrokit; however, as these are not used for this particular setup, they are not included here. The listing of the full package can be viewed here: https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-lopy4-and-sensors-bundle/.

Computer Setup

The IDE used in this setup is Atom and the pymakr plugin – one may use other IDEs such as Visual Studio Code. Instructions for retrieving Atom can be found at https://flight-manual.atom.io/getting-started/sections/installing-atom/. Pymakr lets you upload code written in Atom into the files of the IoT device (to be run when the device is connected/started), as well as downloading the existing code of the device into your Atom project. Furthermore, one can write and execute code directly in the terminal window. The pymakr plugin can be found and installed by doing a search for “pymakr” in the Packages menu option of Atom.

Before setting up the software, you may need to install drivers. This guide is for Mac users and drivers are not needed, however, drivers for Windows and Linux may be found here: https://docs.pycom.io/gettingstarted/installation/drivers/.

You may choose to update the firmware of the expansion board before going further, although this should not be necessary with v3.1. This is a slightly more complicated process as it requires some work in the Terminal/Command Line Interface. Instructions can be found at: https://docs.pycom.io/gettingstarted/installation/firmwaretool/.

To set up the initial connection between the device and your computer, as well as flashing the firmware, simply connect the device via the USB cable and open pymakr in Atom. Alternatively, you can download an application called Pycom Firmware Update (found here: https://pycom.io/downloads/) and simply follow the instructions. Note that the LoPy4 must be mounted on the expansion board, and the antenna connected to the LoPy4 antenna port, before attempting this stage.

Connect to the USB port and initialize the setup with your chosen application. If all goes well, you will be asked to provide a serial number for the registration of the device. To get this serial number, create an account at https://pybytes.pycom.io/, the cloud platform that will receive the temperature data that your device generates. You get a serial key by creating a new device in the menu. Enter this serial key into pymakr or Pycom Firmware Update and the setup is complete.

To connect the LoPy4 wirelessly to the Pybytes cloud, you need to add your WiFi credentials, and if you want to connect through LoRa/SigFox, you may need to create an account at https://docs.pycom.io/pybytes/networks/sigfox/ to receive SigFox credentials. These connections are added in Pybytes under the Configure Networks option in the main menu.

If any of the above is unclear, more detailed instructions on the hardware and software setup can be found in the Pycom documentation at https://docs.pycom.io/gettingstarted/.

Putting everything together

In this section I briefly describe how all the hardware is connected.

The LoPy4 is mounted on top of the expansion board. The module should fit on the board such that the “pycom” text on both components should face the same side.
The expansion board is connected to the computer via a Micro USB cable.
The antenna is connected to the 868/915 LoRa/SigFox antenna port of the LoPy4. There are two antenna ports on the module; choose the one on the same side as the LED light.
The three leads of the sensor are connected to three corresponding circuits on the expansion board by way of a breadboard and wires, as such:
P16 connects to the middle pin.
3V3 connects to the left pin.
GND connects to the right pin.
For more detailed instructions on the basic hardware setup (minus the breadboard and sensor components), visit https://docs.pycom.io/gettingstarted/connection/lopy4/.

The following is a circuit diagram showing how the electronics is connected:

![image](https://user-images.githubusercontent.com/49246098/110234331-36392200-7f2a-11eb-872b-9f0a474d3e14.png)


Platform

This project uses the Pybytes 2.0 cloud platform. This platform is specifically made for the management of Pycom development boards and modules. You can manage devices, network connections, projects, and present/store/manipulate any data sent from the devices. You can also work in pymakr through this platform. Learn more at https://pycom.io/products/software/pybytes-3/.

The Code

Here I will provide the Python programming code that executes the behavior that makes up the purpose of the IoT device. It is short, simple and looks like so:

![image](https://user-images.githubusercontent.com/49246098/110234341-3d603000-7f2a-11eb-9ca8-e023a862b415.png)


The following code executes when the device is run. Firstly, the libraries pycom, machine and time are imported to provide us with useful methods. Secondly, the string "temperature readings" is printed in the terminal window of pymakr. Thirdly, an infinite loop is created through while True. This loop executes the following commands:

Generate and calculate the temperature reading from the sensor and assign it to the variable celcius.
Print the value of celcius in the terminal window.
Establish a connection with the method send_signal() from the pybytes library, and send the value of celcius to signal 1. This signal will be received by the Pybytes platform.
Pause the program for five seconds using the method provided by the time library.
The output in the pymakr terminal will be something like this:

![image](https://user-images.githubusercontent.com/49246098/110234348-4cdf7900-7f2a-11eb-80f4-d4c55f5bcb41.png)


Transmitting the data / connectivity

The temperature data generated by the sensor is sent every five seconds as explained in the preceding section, by way of an infinite While-loop and a five second pause.

The wireless protocol used to send the data from the LoPy4 to Pybytes is WiFi. The transport protocol used is MQTT.

Presenting the data

Here is a screenshot of the simple yet informative temperature data as it is presented in the Pybytes dashboard. The date, time and size of the data, and the temperature reading itself, are shown in a table, like so:

![image](https://user-images.githubusercontent.com/49246098/110234360-58cb3b00-7f2a-11eb-88fa-384ff0ba4c74.png)


Above the dashboard, the device information can be seen, such as the name (SAME-SILK-4014), device model, firmware version, last connection made, and the serial key. The data coming from the IoT device is called Signal 1; if we were to send other kinds of data from other sensors, we would establish additional signals in MicroPython.

The data sits in the Pybytes database for one month; this may be extended or manipulated through integrations with third-party cloud platforms, see the following: https://pybytes.pycom.io/integrations/add.

Finalizing the design

The IoT device itself looks like this:


![Skärmavbild 2021-03-07 kl  09 50 27](https://user-images.githubusercontent.com/49246098/110234400-8d3ef700-7f2a-11eb-96e6-c5497e1e161b.png)


Visible above is the development board, the expansion board, the antenna, the breadboard, the sensor (the tiny black component on the breadboard) and the jumper wires. This device does what it was intended to do: it collects sensory input in the form of temperature, converts it to information, and sends it to an external cloud platform in a user-friendly way.

This is a very minimalistic project, intended for a beginner level exploration of what IoT devices look like, how they work, how they are assembled and programmed. For those who have more time and resources, many improvements can be made:

Adjust the temperature reading presented in the Pybytes dashboard to remove the overabundant decimals.
Collect and calculate more data, such as Fahrenheit readings, temperature changes over time, etc.
The addition of other sensors; the breadboard provides ample room for this.
For any one interested in IT and programming, like me, this is a very interesting project. It is great to learn exactly how programming can be done on things that are not computers and laptops, and it is fascinating to see how sensor input from the real world is made into digital information, and how simple it is to do oneself.
