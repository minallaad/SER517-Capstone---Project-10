# Pysimulavr


Pysimulavr is a python wrapper over original simulavr package that was created in C++

  - It is based on Python3
  - It enables the simulator GUI to be run using PyQt5
  - Currently supports Ubuntu Linux




### Dependencies

Pysimulavr uses a number of open source projects to work properly:

* [Python3](https://docs.python.org/3/tutorial/index.html)- Python3, is an easy to learn, powerful programming language.
* [Sphnix](http://www.sphinx-doc.org/en/master/) - Sphinx, is a tool that makes it easy to create intelligent and beautiful documentation
* [Simulavr](https://github.com/Traumflug/simulavr) - the SimulAVR program is a simulator for the Atmel AVR family of microcontrollers.
* [Ubuntu](https://www.ubuntu.com/) - Ubuntu, is a free and open-source Linux distribution based on Debian

# Simulator GUI

Simulator GUI is a python package that runs the ATMega simulator GUI.

 - It is based on Python3
  - It runs over top of Pysimulavr
  - Has gdb-debugger support
  
### Dependencies

Simulator GUI uses a number of open source projects to work properly:

* [Pysimulavr](hhttps://github.com/minallaad/SER517-Capstone---Project-10) - Pysimulavr is a python wrapper over original simulavr package that was created in C++
* [PyQT5](https://pypi.org/project/PyQt5/) - PyQt5 is a comprehensive set of Python bindings for Qt v5. Qt is set of cross-platform C++ libraries that implement high-level APIs for accessing many aspects of modern desktop and mobile systems

And of course Simulator GUI itself is open source with a  [public repository](https://github.com/minallaad/SER517-Capstone---Project-10)
 on GitHub.

## Installation

Simulator GUI requires Ubuntu to run.

Install latest version of Ubuntu from [here](https://www.ubuntu.com/download/desktop) and follow the [instructions](https://tutorials.ubuntu.com/tutorial/tutorial-install-ubuntu-desktop?_ga=2.93148634.63552553.1554758121-1237498257.1554429778#0)

Pip install Python3

```sh
$ sudo apt-get install python3-pip
```
Install Sphinx 

```sh
sudo apt-get install python3-sphinx
```
Git clone the two repositories viz. Simulavr, Simlator GUI

```sh
$ git clone https://github.com/Traumflug/simulavr.git
$ git clone https://github.com/minallaad/SER517-Capstone---Project-10.git
```
Install Pysimulavr

```sh
$sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
$sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 2
$sudo update-alternatives --config python
$cd ~/simulavr
$make distclean
$./bootstrap
$./configure --enable-python --with-pic
$make
$cd src/python/dist
$python -m pip install ./pysimulavr-1.1.dev0-cp36-cp36m-linux_x86_64.whl
```

Install GUI dependencies

```sh
$ cd SER517-Capstone---Project-10/
$ pip install -r requirements.txt 
```

## Starting the GUI

```sh
$ cd SER517-Capstone---Project-10/
$ python3 main.py 
```



### Todos

 - Package the GUI


