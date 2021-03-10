
# robobo-coppelia-simulator

Repository of Robobo robot simulation in the CoppeliaSim environment.

## Requirements

 - Windows, Linux, macOS.
 - CoppeliaSim.
 - Robobo.py library.

## Installation

To install CoppeliaSim in your computer, please follow the instructions at:

https://www.coppeliarobotics.com/downloads

To install the _robobo.py_ library, follow the steps explained at:

https://github.com/mintforpeople/robobo-programming/wiki/python-doc

Finally, download this repository and:

* Copy all the files in the *lib* folder into your *robobo.py-master* folder
* Copy the _models_ and _worlds_ folders to your computer, so you can open them from CoppeliaSim.
* Copy the files in the _scripts_ folder to your computer so you can try the included examples

## Basic usage

Add the *robobo.ttm* CoppeliaSim model to the desired scene and start the simulation, as explained in:

https://www.coppeliarobotics.com/helpFiles/index.html

Open any python IDE and run _RoboboSimulationServer.py_

While Robobo Simulation Server is running, run your own scripts on another terminal. The connection and usage of the simulation model is the same as the real robot, but using the localhost IP:

```bash
from Robobo import Robobo
robobo = Robobo('127.0.0.1')
robobo.connect()
```

The following methods of the _robobo.py_ library are not available yet:
* Camera methods (see next section in order to have an option to use your own camera methods easily) 
* Audio methods

## Camera streaming



## Multi-robot environment

Coming soon.

## Structure

This package contains the following folders and files:
 - lib: remote API files.
 - example.py: connect and interact example script.
 - README.md: this file.
 - robobo.ttm: Robobo CoppeliaSim model.
 - robobo-pusher.ttm: Robobo with pusher tool model.