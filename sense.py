#!/usr/bin/python
from sense_hat import SenseHat

class PiSenseHat(object):
    """Raspberry Pi 'IoT Sense Hat API Driver Class'."""


    # Constructor
    def __init__(self):
        self.sense = SenseHat()
        # enable all IMU functions
        self.sense.set_imu_config(True, True, True)

    def getPressure(self):
        return self.sense.get_pressure()

    def getTemperature(self):
        return self.sense.get_temperature()

    def getHumidity(self):
        return self.sense.get_humidity()

    def getHumidityTemperature(self):
        return self.sense.get_temperature_from_humidity()

    def getPressureTemperature(self):
        return self.sense.get_temperature_from_pressure()

    def getOrientationRadians(self):
        return self.sense.get_orientation_radians()

    def getOrientationDegrees(self):
        return self.sense.get_orientation_degrees()

    def getCompass(self):
        return self.sense.get_compass()

    def getAccelerometer(self):
        return self.sense.get_accelerometer_raw()

    def getEnvironmental(self):
        sensors = {'name' : 'sense-hat', 'environmental':{}}
        return sensors

    def getJoystick(self):
        sensors = {'name' : 'sense-hat', 'joystick':{}}
        return sensors

    def getInertial(self):
        sensors = {'name' : 'sense-hat', 'inertial':{}}
        return sensors

    # Add API for each sensor
    def getAllSensors(self):
        sensors = {'name' : 'sense-hat', 'environmental':{}, 'inertial':{}, 'joystick':{}}
        sensors['environmental']['pressure'] = { 'value':self.sense.get_pressure(), 'unit':'mbar'}
        sensors['environmental']['temperature'] = { 'value':self.sense.get_temperature(), 'unit':'C'}
        sensors['environmental']['humidity'] = { 'value':self.sense.get_humidity(), 'unit': '%RH'}
        accel = self.sense.get_accelerometer_raw()
        sensors['inertial']['accelerometer'] = { 'x':accel['x'], 'y':accel['y'], 'z':accel['z'], 'unit':'g'}
        orientation = self.sense.get_orientation_degrees()
        sensors['inertial']['orientation'] = { 'compass':self.sense.get_compass(), 'pitch':orientation['pitch'], 'roll':orientation['roll'], 'yaw':orientation['yaw'], 'unit':'degress'}
        return sensors


def main():

    # Create instance of pi Sense-Hat sensor object
    pi_sense_hat = PiSenseHat()

    # Read Parameters
    p = pi_sense_hat.getPressure()
    t_c = pi_sense_hat.getTemperature()
    h = pi_sense_hat.getHumidity()
    ht = pi_sense_hat.getHumidityTemperature()
    hp = pi_sense_hat.getPressureTemperature()
    orientation = pi_sense_hat.getOrientationDegrees()
    accel = pi_sense_hat.getAccelerometer()
    d = pi_sense_hat.getCompass()

    #print("================ Discrete Sensor Values ==================")
    #print("      Pressure :", p)
    #print("   Temperature :", t_c)
    #print("      Humidity :", h)
    #print("  HumidityTemp :", ht)
    #print("  PressureTemp :", hp)
    #print("       Compass :", d)
    #print("  p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
    #print("  x: {x}, y: {y}, z: {z}".format(**accel))
    #print("==========================================================\n")

    #print("================== Dictionary Object =====================")
    #print(pi_sense_hat.getAllSensors())
    #print("==========================================================\n")

if __name__=="__main__":
    main()
