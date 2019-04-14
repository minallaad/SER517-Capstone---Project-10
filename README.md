# SER517-Capstone---Project-10 with Professor Douglas


**Members**

Ayan Shah

Minal Laad

Ruihao Zhou

Kaustuv Deolal

Saheb Johar

Aman Maheshwari

## Overview
<table>
<tr>
<td>
The brief requirement of client was to develop a clock accurate simulator which can simulate the microcontroller Atmega328P and provide a graphical visualization for the same. However, with the availability of Simulavr - simulator for AVR Microcontrollers, the project scope was reduced down to the development of the graphical visualization for Simulavr. The client requires a GUI which can display the current state of the ATMEGA328 microcontroller being simulated by Simulavr.  The problem statement of the project is to create a GUI which displays the internal states and values of the various components of the microcontroller. The application should allow the users to debug programs for Atmega328 (simulated device) using a debugger, specifically GDB. The final deliverable must consist of a GUI which displays the data of the internal states of the microcontroller throughout the program debugging. The GUI must be able to fetch the updated states of the microcontroller pins, registers and other components and should display it to the users. The project is focused on helping students working on microcontroller programming for simulation purposes.
</td>
</tr>
</table>

## Requirement
<table>
<tr>
<td>
For this project, the product owner Dr. Douglas Sandy, has outlined a few key requirements which he would like to have. These requirements are: The GUI should be able to show the states and register values of Atmega328 specific components such as: GPIO Ports, Pin States, EEPROM, USART, 16 Bit and 2 8 Bit Timers, SPI Register, and GPIO Registers. GUI Layouts should be interactive and intuitive to the users who have experienced working with microcontrollers and it’s diagrams. The GUI should have navigations to different microcontroller components available through Simulavr. The GUI application should be able to interface with simulavr in parallel with GDB so that the users can use the application when debugging on Simulavr. Open an interface with Simulavr to fetch the required data for the microcontroller. Allow users to view the console outputs of the program running on Simulator.
The above list of requirements broadly list out all the necessary features of the project and what it’s final outcome should be.
</td>
</tr>
</table>

## Tools

[Pycharm IDE](https://www.jetbrains.com/pycharm/) - We require this IDE to help us better understand the code base for pysimulavr, as it provides easy run configuration options and good debugging to view runtime data.

[Codeblocks](http://www.codeblocks.org/) - The IDE is required to build and run AVR code with Simulavr.

[Wireshark](https://www.solarwinds.com/free-tools/response-time-viewer-for-wireshark?&CMP=KNC-TAD-GGL-SW_NA_X_PP_CPC_LD_EN_PRODE_DWA-FXNET-982238371~47089245085_g_c_wireshark-e~311972701385~~&ds_cid=71700000047472276&ds_agid=58700004762384593&network=g&device=c&keyword=Wireshark&matchtype=e&creative=311972701385&feeditemid=&gclid=CjwKCAjwqLblBRBYEiwAV3pCJsGS5VyzI4uZv9t4Gt0TOMUX1so0L0jhll_V9zJFfzZ2WghSH7CpdBoCQMYQAvD_BwE) - This tool is used to trace packets between Simulavr and GDB, and also UI port 7777 to understand how simulavr sends data over a socket connection.

[Virtual Box](https://www.virtualbox.org/)- The development process is being done in a Linux environment, thus we require a virtual Linux environment in our Windows/Mac environments.

[Adobe XD](https://www.adobe.com/products/xd.html?sdid=12B9F15S&mv=Search&ef_id=CjwKCAjwqLblBRBYEiwAV3pCJn7wWU_6f28aW9etyuLHvPFLTGp_FmIsOYplz3kMfpxrvo0BQs2yvRoCUboQAvD_BwE:G:s&s_kwcid=AL!3085!3!315233774112!e!!g!!adobe%20xd) - Tool used to create the wireframe designs for the GUI.

[Avr Tool chain](https://www.microchip.com/mplab/avr-support/avr-and-arm-toolchains-c-compilers)- Required libraries and compiler tool chain to execute Simulavr and GDB

[Slack](https://slack.com) brings all your communication together in one place. It's real-time messaging, archiving and search for modern teams.


## Installation Direction

Run this command to install PyQt5：

```
$  sudo apt-get install python3-pyqt5
```

Run this command to install Pysimulavr：

```
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.61
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.72
$ sudo update-alternatives --config python
$ cd simulavr
$ ./bootstrap
$ ./configure --enable-python
$ Make
$ Sudo python setup.py install
$ Python --version
$ In ./bash_profile add $LD_LIBRARY_PATH = /usr/local/lib/
$ python
$ Import pysimulavr
```

Install GUI dependencies:

```
$ cd SER517-Capstone---Project-10/
$ pip install -r requirements.txt
```

## Build and Run Directions

```
$ cd SER517-Capstone---Project-10/
$ python3 main.py
```
## Design Details




