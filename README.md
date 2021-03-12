
# robobo-coppelia-simulator

Repository of Robobo robot simulation in the CoppeliaSim environment.


## Repository contents

- lib: it includes all the python libraries to run Robobo in CoppeliaSim using robobo.py
- models: it includes the Robobo models for CoppeliaSim. *robobo_pusher* corresponds to the model with pusher
- worlds: it includes different simulation environments to be used with Robobo
- example.py: a simple example that makes Robobo move in a closed environment avoiding walls

## Requirements

- Windows, Mac or Linux computer (GPU recommended)
- CoppeliaSim
- Robobo.py library

## Installation

To install CoppeliaSim in your computer, please follow the instructions at:

https://www.coppeliarobotics.com/downloads

To install the _robobo.py_ library, follow the steps explained at:

https://github.com/mintforpeople/robobo-programming/wiki/python-doc

Finally, download this repository and:

* Copy all the files of the *lib* folder into your *robobo.py-master* or *robobo.py* folder
* Copy the _models_ and _worlds_ folders to your computer, so you can open them from CoppeliaSim.
* Copy the example.py file in your computer so you can try it.

## Basic usage

Add the *robobo.ttm* CoppeliaSim model to the desired scene and start the simulation, as explained in:

https://www.coppeliarobotics.com/helpFiles/index.html

Open any python IDE and run the _RoboboSimulationServer.py_ script.

While Robobo Simulation Server is running, run your own scripts on another terminal. The connection and usage of the simulation model is the same as the real robot, but using the localhost IP:

```bash
from Robobo import Robobo
robobo = Robobo('127.0.0.1')
robobo.connect()
```

The following methods of the _robobo.py_ library are not available yet:
* Camera methods
* Audio methods

## Camera streaming

Coming soon.

## Multi-robot environment

Coming soon.