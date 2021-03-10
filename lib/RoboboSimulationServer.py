import asyncio
import websockets
import json
from RoboboSim import RoboboSim


class RoboboSimulationServer:

    def __init__(self):
        print("Ejecutando servidor websockets")
        # si se quieren usar varios robots en simulacion habra que usar puertos diferentes y que la libreria
        # pueda configurarse asi, cosa que no hace porque los robots reales usan el mismo puerto pero diferentes ips
        self.port = 40404
        self.outgoing = asyncio.Queue()
        self.id = ""
        self.sensor_delay = 0.333  # sensor delay in seconds
        self.sim_plugin = RoboboSim()
        start_server = websockets.serve(self.handler, 'localhost', self.port)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    def process_message(self, status):
        name = status["name"]
        parameters = status["parameters"]
        self.id = status["id"]
        if name == "SET-SENSOR-FREQUENCY":
            frequency = parameters["frequency"]
            self.set_sensor_frecuency(frequency)
        elif name == "MOVE":
            self.move_wheels(parameters)
        elif name == "MOVE-BLOCKING":
            self.move_wheels_blocking(parameters)
        elif name == "MOVEBY-DEGREES":
            self.move_wheels_by_degrees(parameters)
        elif name == "MOVEPAN":
            self.move_pan(parameters)
        elif name == "MOVEPAN-BLOCKING":
            self.move_pan_blocking(parameters)
        elif name == "MOVETILT":
            self.move_tilt(parameters)
        elif name == "MOVETILT-BLOCKING":
            self.move_tilt_blocking(parameters)
        elif name == "SET-LEDCOLOR":
            self.set_led_color(parameters)
        elif name == "RESET-WHEELS":
            self.reset_wheels()
        elif name == "SET-EMOTION":
            self.set_emotion(parameters)

    def set_sensor_frecuency(self, frequency):
        # time in seconds
        if frequency == "LOW":
            self.sensor_delay = 1
        elif frequency == "NORMAL":
            self.sensor_delay = 0.333
        elif frequency == "HIGH":
            self.sensor_delay = 0.1
        elif frequency == "MAX":
            self.sensor_delay = 0.01
      
    def unlock(self, blockid, command):
        self.sim_plugin.block()
        parameters_to_send = {'blockid': blockid}
        unlock_message = self.encode_message(command, parameters_to_send)
        self.outgoing.put_nowait(unlock_message)

    def move_wheels(self, parameters):
        lspeed = int(parameters["lspeed"])
        rspeed = int(parameters["rspeed"])
        time = float(parameters["time"])
        self.sim_plugin.moveWheelsByTime(rspeed, lspeed, time)
        wheels_message = self.read_wheels()
        self.outgoing.put_nowait(wheels_message)

    def move_wheels_by_degrees(self, parameters):
        wheel = parameters["wheel"]
        speed = int(parameters["speed"])
        degrees = int(parameters["degrees"])
        self.sim_plugin.moveWheelsByDegrees(wheel, speed, degrees)
        blockid = parameters["blockid"]
        self.unlock(blockid, "UNLOCK-MOVE")
        wheels_message = self.read_wheels()
        self.outgoing.put_nowait(wheels_message)

    def move_wheels_blocking(self, parameters):
        self.move_wheels(parameters)
        blockid = parameters["blockid"]
        self.unlock(blockid, "UNLOCK-MOVE")
        wheels_message = self.read_wheels()
        self.outgoing.put_nowait(wheels_message)

    def move_pan(self, parameters):
        pos = int(parameters["pos"])
        speed = int(parameters["speed"])
        self.sim_plugin.movePanTo(pos, speed)
        pan_message = self.read_pan_position()
        self.outgoing.put_nowait(pan_message)

    def move_pan_blocking(self, parameters):
        self.move_pan(parameters)
        blockid = parameters["blockid"]
        self.unlock(blockid, "UNLOCK-PAN")
        pan_message = self.read_pan_position()
        self.outgoing.put_nowait(pan_message)

    def move_tilt(self, parameters):
        pos = int(parameters["pos"])
        speed = int(parameters["speed"])
        self.sim_plugin.moveTiltTo(pos, speed)
        tilt_message = self.read_tilt_position()
        self.outgoing.put_nowait(tilt_message)

    def move_tilt_blocking(self, parameters):
        self.move_tilt(parameters)
        blockid = parameters["blockid"]
        self.unlock(blockid, "UNLOCK-TILT")
        tilt_message = self.read_tilt_position()
        self.outgoing.put_nowait(tilt_message)

    def set_led_color(self, parameters):
        led = parameters["led"]
        color = parameters["color"]
        self.sim_plugin.setLEDColor(led, color)
        led_color = 0  # INCOMPLETE
        parameters_to_send = {'all': led_color}
        led_message = self.encode_message("LED", parameters_to_send)
        self.outgoing.put_nowait(led_message)

    def reset_wheels(self):
        self.sim_plugin.resetWheelEncoders()
        wheels_message = self.read_wheels()
        self.outgoing.put_nowait(wheels_message)

    def read_ir_sensor(self):
        ir_sensor_list = self.sim_plugin.readAllIRSensor()
        backl, backr, frontl, frontr, frontc, frontrr, backc, frontll = tuple(ir_sensor_list)
        parameters_to_send = {'Back-L': backl, 'Back-R': backr, 'Front-L': frontl,  'Front-R': frontr,
                              'Front-C': frontc, 'Front-RR': frontrr, 'Back-C': backc, 'Front-LL': frontll}
        return self.encode_message("IRS", parameters_to_send)
    
    def read_wheels(self):
        wheels = self.sim_plugin.readWheels()
        wheelPosR, wheelPosL, wheelSpeedR, wheelSpeedL = tuple(wheels)
        parameters_to_send = {'wheelPosR': wheelPosR, 'wheelPosL': wheelPosL,
                              'wheelSpeedR': wheelSpeedR, 'wheelSpeedL': wheelSpeedL}
        return self.encode_message("WHEELS", parameters_to_send)

    def read_pan_position(self):
        pan_position = self.sim_plugin.readPanPosition()
        parameters_to_send = {'panPos': pan_position}
        return self.encode_message("PAN", parameters_to_send)

    def read_tilt_position(self):
        tilt_position = self.sim_plugin.readTiltPosition()
        parameters_to_send = {'tiltPos': tilt_position}
        return self.encode_message("TILT", parameters_to_send)

    def read_orientation_sensor(self):
        yaw, pitch, roll = self.sim_plugin.readOrientationSensor()
        parameters_to_send = {'yaw': yaw, 'pitch': pitch, 'roll': roll}
        return self.encode_message("ORIENTATION", parameters_to_send)
       
    def read_acceleration_sensor(self):
        xaccel, yaccel, zaccel = self.sim_plugin.readAccelerationSensor()
        parameters_to_send = {'xaccel': xaccel, 'yaccel': yaccel, 'zaccel': zaccel}
        return self.encode_message("ACCELERATION", parameters_to_send)

    def set_emotion(self, parameters):
        emotion = parameters["emotion"]
        self.sim_plugin.setEmotionTo(emotion)
        tilt_message = self.read_tilt_position()  # provisional HELP HELP HELP HELP HELP HELP HELP HELP
        self.outgoing.put_nowait(tilt_message)

    async def consumer_handler(self, websocket, path):
        while True:
            message = await websocket.recv()
            await self.consumer(message)

    async def producer_handler(self, websocket, path):
        while True:
            message = await self.outgoing.get()
            print("Enviando:", message)
            await websocket.send(message)
            self.outgoing.task_done()

    async def sensor_producer(self, websocket, path):
        while True:
            ir_message = self.read_ir_sensor()
            orientation_message = self.read_orientation_sensor()
            acceleration_message = self.read_acceleration_sensor()
            await websocket.send(ir_message)
            await websocket.send(orientation_message)
            await websocket.send(acceleration_message)
            await asyncio.sleep(self.sensor_delay)
    
    async def consumer(self, message):
        # la primera vez me pasan un password, asi que va por la excepcion
        print("Recibiendo:", message)
        try:
            status = json.loads(message)
            self.process_message(status)
        except ValueError:
            return

    async def handler(self, websocket, path):
        consumer_task = asyncio.ensure_future(self.consumer_handler(websocket, path))
        producer_task = asyncio.ensure_future(self.producer_handler(websocket, path))
        sensor_producer_task = asyncio.ensure_future(self.sensor_producer(websocket, path))
        done, pending = await asyncio.wait(
            [consumer_task, producer_task, sensor_producer_task],
            return_when=asyncio.FIRST_COMPLETED,)
        for task in pending:
            task.cancel()

    def encode_message(self, name, parameters):
        st = "{\"name\":"
        st += "\"" + name + "\","
        st += "\"value\":{"
        for key in parameters.keys():
            st += "\""+key+"\":"+"\""+str(parameters[key])+"\","
        st = st[:-1]
        st += "}, \"id\":\""+self.id+"\"}"
        return st


if __name__ == "__main__":
    rob = RoboboSimulationServer()
