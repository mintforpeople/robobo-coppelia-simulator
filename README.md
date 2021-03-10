
# robobo-coppelia-simulator

Repository of Robobo robot simulation in the CoppeliaSim environment.

## Requirements

 - Windows, Linux, macOS.
 - CoppeliaSim.
 - Robobo.py library.
 - (Optional) Anaconda3.

## Installation

This model uses the *robobo.py* library. If you dont have it yet, *install and start using* documentation are avaliable on:
https://github.com/mintforpeople/robobo.py

Clone or download this repository and put the *lib* files into your *robobo.py-master* folder.
**Python 3, websockets** and **websocket-client** needs to be installed.

Althoug having Anaconda is not a requirement in order to install and use this model, it is highly recommended doing so due to its simplicity.

With Anaconda you can create a virtual environment with all the dependencies by running:

```bash
conda create -n robobo python=3.6 websockets websocket-client
```

## Basic usage

Add the *robobo.ttm* CoppeliaSim model to the desired scene and start the simulation.

Open any python IDE and run RoboboSimulationServer.py

While Robobo Simulation Server is running, run your own scripts on another terminal. The connection and usage of the simulation model is the same as the real robot:

```bash
from Robobo import Robobo
robobo = Robobo('127.0.0.1')
robobo.connect()
```

To interact with the model, you can use the following functions.

List of robobo.py functions available on simulation:
 - wait
 - moveWheels
 - moveWheelsByTime
 - moveWheelsByDegrees
 - stopMotors
 - movePanTo
 - moveTiltTo
 - setLedColorTo
 - resetWheelEncoders
 - setEmotionTo
 - readAllIRSensor
 - readOrientationSensor
 - readAccelerationSensor
 - readPanPosition
 - readTiltPosition
 - readWheelPosition
 - readWheelSpeed
 - changeStatusFrequency


## Multi-robot environment

Coming soon.

## Structure

This package contains the following folders and files:
 - lib: remote API files.
 - example.py: connect and interact example script.
 - README.md: this file.
 - robobo.ttm: Robobo CoppeliaSim model.
 - robobo-pusher.ttm: Robobo with pusher tool model.