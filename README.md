# SER517-Capstone---Project-10 with Professor Douglas


## Overview
<table>
<tr>
<td>
The project focuses on creating a GUI which provides a graphical visualization of the internal simulation of the ATMEGA328P microcontroller.  Simulavr is used for the simulation of AVR microcontrollers. The GUI is required to fetch the current state of the microcontroller including Port and DDR registers, and components of the microcontroller. The users are allowed to debug their program through Codeblocks or external GDB application and view the updated state of microcontroller on the GUI.
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

## Component Diagram
<img src="/Resources/Images/Architecture_Diagram.png">

## Tools

[Pycharm IDE](https://www.jetbrains.com/pycharm/) - We require this IDE to help us better understand the code base for pysimulavr, as it provides easy run configuration options and good debugging to view runtime data.

[Codeblocks](http://www.codeblocks.org/) - The IDE is required to build and run AVR code with Simulavr.

[Wireshark](https://www.solarwinds.com/free-tools/response-time-viewer-for-wireshark?&CMP=KNC-TAD-GGL-SW_NA_X_PP_CPC_LD_EN_PRODE_DWA-FXNET-982238371~47089245085_g_c_wireshark-e~311972701385~~&ds_cid=71700000047472276&ds_agid=58700004762384593&network=g&device=c&keyword=Wireshark&matchtype=e&creative=311972701385&feeditemid=&gclid=CjwKCAjwqLblBRBYEiwAV3pCJsGS5VyzI4uZv9t4Gt0TOMUX1so0L0jhll_V9zJFfzZ2WghSH7CpdBoCQMYQAvD_BwE) - This tool is used to trace packets between Simulavr and GDB, and also UI port 7777 to understand how simulavr sends data over a socket connection.

[Virtual Box](https://www.virtualbox.org/)- The development process is being done in a Linux environment, thus we require a virtual Linux environment in our Windows/Mac environments.

[Adobe XD](https://www.adobe.com/products/xd.html?sdid=12B9F15S&mv=Search&ef_id=CjwKCAjwqLblBRBYEiwAV3pCJn7wWU_6f28aW9etyuLHvPFLTGp_FmIsOYplz3kMfpxrvo0BQs2yvRoCUboQAvD_BwE:G:s&s_kwcid=AL!3085!3!315233774112!e!!g!!adobe%20xd) - Tool used to create the wireframe designs for the GUI.

[Avr Tool chain](https://www.microchip.com/mplab/avr-support/avr-and-arm-toolchains-c-compilers)- Required libraries and compiler tool chain to execute Simulavr and GDB

[Slack](https://slack.com) brings all your communication together in one place. It's real-time messaging, archiving and search for modern teams.


## Installation Direction

Build and install the toolds rquired：

```
$  sudo apt install gcc make git
$  sudo apt-get install build-essential g++ libtool-bin binutils-dev texinfo autoconf swig
$  sudo apt-get --purge remove gdb-avr
$  wget ftp.gnu.org/gnu/gdb/gdb-8.1.1.tar.xz
$  tar xf gdb-8.1.1.tar.xz
$  cd gdb-8.1.1
$  perl -i -0pe 's/  ULONGEST addr = unpack_long \(type, buf\);\R\R  return avr_make_saddr \(addr\);\R/  ULONGEST addr = unpack_long (type, buf);\n\n  if (TYPE_DATA_SPACE (type))\n    return avr_make_saddr (addr);\n  else\n    return avr_make_iaddr (addr);\n/' gdb/avr-tdep.c
```

Run this command to install Pysimulavr：

```
$ sudo apt-get install python3.6
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

Installation Pysimulavr Module:

```
$ git clone https://git.savannah.gnu.org/git/simulavr.git/
$ cd simulavr
$ sudo apt-get install python3-pip
$ sudo apt-get install python3-sphinx
$ sudo apt-get install python3-pyqt5
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 2
$ sudo update-alternatives --config python
$ make distclean
$ ./bootstrap
$ ./configure --enable-python --with-pic
$ make
$ cd src/python/dist
$ python -m pip install ./pysimulavr-1.1.dev0-cp36-cp36m-linux_x86_64.whl
```

## Build and Run Directions

```
$ git clone https://github.com/minallaad/SER517-Capstone---Project-10.git
$ cd (folder)
$ python3 main.py
```
## Design Details
* **[Two modules]**
  * [Front-End] landing page consists of various UI components like Ports and Registers which are dynamically updated. The user can click on different components to view their circuit diagrams and updated register states. 
  * [Back-End] adaptor communicates with a python interface (Pysimulavr - as shown in Fig.1) which was built using SWIG, Â to interact with native C++ code of simulavr. The backend adaptor uses pysimulavr to create an avr device object using the build file provided by codeblocks. The adaptor runs endlessly, simulating each clock cycle and fetches the updated values using the functions provided by the device object. The simulator values are translated to hexadecimal format to conform to the simulator model.


## Main Page
<img src="/Resources/Images/MainPicturePage.png">

## Running Demo
[![](http://img.youtube.com/vi/5v_OvZfBDK4/0.jpg)](http://www.youtube.com/watch?v=5v_OvZfBDK4 "eepromUI")


## Contributors

These people are responsible for developing the AtMega328 simulator in Python:

- [Aman Maheshwari](https://github.com/aman25m)

- [Ayan Shah](https://github.com/arshah12)

- [Kaustuv Deolal](https://github.com/Vutsuak16)

- [Minal Laad](https://github.com/minallaad)

- [Saheb Johar](https://github.com/sahebjohar92)

- [Ruihao Zhou ](https://github.com/Parsons-Ray>)
