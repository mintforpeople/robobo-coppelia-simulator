import time
try:
    import sim
except:
    print('--------------------------------------------------------------')
    print('"sim.py" could not be imported. This means very probably that')
    print('either "sim.py" or the remoteApi library could not be found.')
    print('Make sure both are in the same folder as this file,')
    print('or appropriately adjust the file "sim.py"')
    print('--------------------------------------------------------------')
    print('')


class RoboboSim:

    def __init__(self):
        sim.simxFinish(-1)  # just in case, close all opened connections
        self.clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
        if self.clientID != -1:
            print('Connected to remote API server')
        else:
            print('Failed connecting to remote API server')

    def block(self):
        res = sim.simxGetIntegerSignal(self.clientID, 'Bloqueado', sim.simx_opmode_blocking)
        while res[1]:
            time.sleep(0.1)
            res = sim.simxGetIntegerSignal(self.clientID, 'Bloqueado', sim.simx_opmode_blocking)

    def moveWheelsByTime(self, rspeed, lspeed, duration):
        inputIntegers = [rspeed, lspeed]
        inputFloats = [duration]
        inputStrings = []
        inputBuffer = bytearray()
        sim.simxCallScriptFunction(self.clientID, 'Left_Motor', sim.sim_scripttype_childscript, 'moveWheelsByTime',
                                   inputIntegers, inputFloats, inputStrings, inputBuffer, sim.simx_opmode_blocking)

    def moveWheelsByDegrees(self, wheel, degrees, speed):

        inputIntegers = [degrees, speed]
        inputFloats = []
        inputStrings = [wheel]
        inputBuffer = bytearray()
        sim.simxCallScriptFunction(self.clientID, 'Left_Motor', sim.sim_scripttype_childscript, 'moveWheelsByDegrees',
                                   inputIntegers, inputFloats, inputStrings, inputBuffer, sim.simx_opmode_blocking)

    def movePanTo(self, degrees, speed):
        inputIntegers = [degrees, speed]
        inputFloats = []
        inputStrings = []
        inputBuffer = bytearray()
        sim.simxCallScriptFunction(self.clientID, 'Pan_Motor', sim.sim_scripttype_childscript, 'movePanTo',
                                   inputIntegers, inputFloats, inputStrings, inputBuffer, sim.simx_opmode_blocking)

    def moveTiltTo(self, degrees, speed):
        inputIntegers = [degrees, speed]
        inputFloats = []
        inputStrings = []
        inputBuffer = bytearray()
        sim.simxCallScriptFunction(self.clientID, 'Tilt_Motor', sim.sim_scripttype_childscript, 'moveTiltTo',
                                   inputIntegers, inputFloats, inputStrings, inputBuffer, sim.simx_opmode_blocking)

    def setLEDColor(self, led, color):
        inputIntegers = []
        inputFloats = []
        inputStrings = [led, color]
        inputBuffer = bytearray()
        sim.simxCallScriptFunction(self.clientID, 'Back_L', sim.sim_scripttype_childscript, 'setLEDColor',
                                   inputIntegers, inputFloats, inputStrings, inputBuffer, sim.simx_opmode_blocking)

    def readAllIRSensor(self):
        inputIntegers = []
        inputFloats = []
        inputStrings = []
        inputBuffer = bytearray()
        array = sim.simxCallScriptFunction(self.clientID, 'IR_Back_C', sim.sim_scripttype_childscript,
                                           'readAllIRSensor', inputIntegers, inputFloats, inputStrings, inputBuffer,
                                           sim.simx_opmode_blocking)
        return array[1]

    def readPanPosition(self):
        inputIntegers = []
        inputFloats = []
        inputStrings = []
        inputBuffer = bytearray()
        array = sim.simxCallScriptFunction(self.clientID, 'Pan_Motor', sim.sim_scripttype_childscript,
                                           'readPanPosition', inputIntegers, inputFloats, inputStrings,
                                           inputBuffer, sim.simx_opmode_blocking)
        return array[1][0]

    def readTiltPosition(self):
        inputIntegers = []
        inputFloats = []
        inputStrings = []
        inputBuffer = bytearray()
        array = sim.simxCallScriptFunction(self.clientID, 'Tilt_Motor', sim.sim_scripttype_childscript,
                                           'readTiltPosition', inputIntegers, inputFloats, inputStrings,
                                           inputBuffer, sim.simx_opmode_blocking)
        return array[1][0]

    def readWheels(self):
        inputIntegers = []
        inputFloats = []
        inputStrings = []
        inputBuffer = bytearray()
        array = sim.simxCallScriptFunction(self.clientID, 'Left_Motor', sim.sim_scripttype_childscript, 'readWheels',
                                           inputIntegers, inputFloats, inputStrings, inputBuffer,
                                           sim.simx_opmode_blocking)
        return array[1]

    def readOrientationSensor(self):
        inputIntegers = []
        inputFloats = []
        inputStrings = []
        inputBuffer = bytearray()
        array = sim.simxCallScriptFunction(self.clientID, 'Smartphone_Respondable', sim.sim_scripttype_childscript,
                                           'readOrientationSensor', inputIntegers, inputFloats, inputStrings,
                                           inputBuffer, sim.simx_opmode_blocking)
        return array[2]

    def readAccelerationSensor(self):
        inputIntegers = []
        inputFloats = []
        inputStrings = []
        inputBuffer = bytearray()
        array = sim.simxCallScriptFunction(self.clientID, 'Smartphone_Respondable', sim.sim_scripttype_childscript,
                                           'readAccelerationSensor', inputIntegers, inputFloats, inputStrings,
                                           inputBuffer, sim.simx_opmode_blocking)
        return array[2]

    def resetWheelEncoders(self):
        inputIntegers = []
        inputFloats = []
        inputStrings = []
        inputBuffer = bytearray()
        sim.simxCallScriptFunction(self.clientID, 'Left_Motor', sim.sim_scripttype_childscript, 'resetWheelEncoders',
                                   inputIntegers, inputFloats, inputStrings, inputBuffer, sim.simx_opmode_blocking)

    def setEmotionTo(self, emotion):
        inputIntegers = []
        inputFloats = []
        inputStrings = [emotion]
        inputBuffer = bytearray()
        sim.simxCallScriptFunction(self.clientID, 'Screen', sim.sim_scripttype_childscript, 'setEmotionTo',
                                   inputIntegers, inputFloats, inputStrings, inputBuffer, sim.simx_opmode_blocking)
