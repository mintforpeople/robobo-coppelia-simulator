from Robobo import Robobo
from utils.StatusFrequency import StatusFrequency
from time import time
from utils.Wheels import Wheels
from utils.IR import IR
from utils.Sounds import Sounds
from utils.Emotions import Emotions
from utils.LED import LED
from utils.Color import Color


def robobo():
    # constant values
    closeIRValue = 100
    mediumIRValue = 20
    farIRValue = 5
    speed = 15
    # Movement starts
    rob.movePanTo(90, 20)
    rob.wait(1)
    print('Pan 90: ', rob.readPanPosition())
    rob.movePanTo(-90, 20)
    rob.wait(1)
    print('Pan -90: ', rob.readPanPosition())
    rob.movePanTo(0, 20)
    rob.wait(1)
    print('Pan 0: ', rob.readPanPosition())
    rob.moveTiltTo(5, 20)
    rob.wait(1)
    print('Tilt 5: ', rob.readTiltPosition())
    rob.moveTiltTo(90, 20)
    rob.wait(1)
    print('Tilt 90: ', rob.readTiltPosition())
    rob.moveWheels(speed, speed)
    while (rob.readIRSensor(IR.FrontC) < farIRValue) and (rob.readIRSensor(IR.FrontRR) < farIRValue) and \
            (rob.readIRSensor(IR.FrontLL) < farIRValue):
        rob.wait(0.1)
        print(rob.readAllIRSensor())
    rob.setLedColorTo(LED.All, Color.YELLOW)
    while (rob.readIRSensor(IR.FrontC) < mediumIRValue) and (rob.readIRSensor(IR.FrontRR) < mediumIRValue) and \
            (rob.readIRSensor(IR.FrontLL) < mediumIRValue):
        rob.wait(0.1)
        print(rob.readAllIRSensor())
    rob.setLedColorTo(LED.All, Color.RED)
    while (rob.readIRSensor(IR.FrontC) < closeIRValue) and (rob.readIRSensor(IR.FrontRR) < closeIRValue) and \
            (rob.readIRSensor(IR.FrontLL) < closeIRValue):
        rob.wait(0.1)
        print(rob.readAllIRSensor())
    rob.moveWheels(0, 0)
    rob.wait(1)
    print('Wheel R: ', rob.readWheelPosition(Wheels.R))
    rob.moveWheelsByTime(-speed, -speed, 3)
    rob.wait(0.1)
    rob.moveWheelsByTime(speed, 0, 2)
    rob.wait(0.1)
    rob.moveWheelsByTime(speed, speed, 5)


if __name__ == '__main__':
    rob = Robobo('127.0.0.1')  # localhost
    rob.connect() 
    rob.changeStatusFrequency(StatusFrequency.Max)
    start_time = time()
    robobo()
    elapsed_time = time() - start_time
    print("Elapsed time: %.3f seconds." % elapsed_time)
