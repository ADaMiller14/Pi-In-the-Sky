# Aidan & Cade's UP house code

# Variables to define
autosave = 10 #                            "autosave" defines the amount of time between saves of the file
maxh = 1#                                "maxh" defines the height (in metres) at which the servo will activated
txt = '/home/pi/Documents/Engineering_4_Notebook/piinthesky/Pi_in_the_Sky_Final'+ +'.txt' # "txt" defines the name of the document used to record the data

# Libraries to import
import smbus
import time
import Adafruit_LSM303
import RPi.GPIO as GPIO

# Setup for the accelerometer, servo, and text writer
lsm303 = Adafruit_LSM303.LSM303()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
p = GPIO.PWM(11, 50)
p.start(0)
f = open(str(txt),'r+')

# Allows the components to be used with measurements that can be relied upon and sets the "launch" time
time.sleep(5)
t0 = time.time()

# Get I2C bus
bus = smbus.SMBus(1)

# MPL3115A2 address, 0x60(96)
# Select control register, 0x26(38)
#		0xB9(185)	Active mode, OSR = 128, Altimeter mode
bus.write_byte_data(0x60, 0x26, 0xB9)
# MPL3115A2 address, 0x60(96)
# Select data configuration register, 0x13(19)
#		0x07(07)	Data ready event enabled for altitude, pressure, temperature
bus.write_byte_data(0x60, 0x13, 0x07)
# MPL3115A2 address, 0x60(96)
# Select control register, 0x26(38)
#		0xB9(185)	Active mode, OSR = 128, Altimeter mode
bus.write_byte_data(0x60, 0x26, 0xB9)

time.sleep(1)

# MPL3115A2 address, 0x60(96)
# Read data back from 0x00(00), 6 bytes
# status, tHeight MSB1, tHeight MSB, tHeight LSB, temp MSB, temp LSB
data = bus.read_i2c_block_data(0x60, 0x00, 6)

# Convert the data to 20-bits
tHeight = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
altitude = tHeight / 16.0

# Sets initial altitude and prints it for debugging
a0 = altitude
print('a0: ' + str(a0) + '\n')

bus.write_byte_data(0x60, 0x26, 0x39)
time.sleep(1)
data = bus.read_i2c_block_data(0x60, 0x00, 4)

while True:
# This loop begins with an exact copy of the altimeter reading
    bus.write_byte_data(0x60, 0x26, 0xB9)
    bus.write_byte_data(0x60, 0x13, 0x07)
    bus.write_byte_data(0x60, 0x26, 0xB9)
    time.sleep(1)
    data = bus.read_i2c_block_data(0x60, 0x00, 6)
    tHeight = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
    temp = ((data[4] * 256) + (data[5] & 0xF0)) / 16
    altitude = tHeight / 16.0
    cTemp = temp / 16.0
    fTemp = cTemp * 1.8 + 32

# Prints altitude record for debugging and sets the "delta-a", as it were, to the variable "a"
    print('altitude: ' + str(altitude))
    a = altitude - a0
    print('delta-a: ' + str(a))

# Immediately checks to see if the house has reached the max altitude
    if a >= maxh:
        p.ChangeDutyCycle(3) # Moves the servo to release balloons
        time.sleep(3)
        p.ChangeDutyCycle(0)
        p.stop()
        GPIO.cleanup() #       Turns the servo off

# MPL3115A2 address, 0x60(96)
# Select control register, 0x26(38)
#		0x39(57)	Active mode, OSR = 128, Barometer mode
    bus.write_byte_data(0x60, 0x26, 0x39)

    time.sleep(1)

# MPL3115A2 address, 0x60(96)
# Read data back from 0x00(00), 4 bytes
# status, pres MSB1, pres MSB, pres LSB
    data = bus.read_i2c_block_data(0x60, 0x00, 4)

# Convert the data to 20-bits
    pres = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
    pressure = (pres / 4.0) / 1000.0

# Output data to screen for debugging
#    print("Pressure : %.2f kPa" %pressure)
#    print("Altitude : %.2f m" %a)
#    print("Temperature in Celsius  : %.2f C" %cTemp)
#    print("Temperature in Fahrenheit  : %.2f F" %fTemp)

# Sets the time since "launch" and converts it to hh:mm:ss format
    elapsed = -1*(int(t0) - int(time.time()))
    T = time.strftime('%H:%M:%S', time.gmtime(elapsed))

# Reads the 5accelerometer and formats the data to m/s^2
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    x = int(accel_x) * (9.81/1024)
    y = int(accel_y) * (9.81/1024)
    z = int(accel_z) * (9.81/1024)
    x = round(x, 3)
    y = round(y, 3)
    z = round(z, 3)

# Creates a special string for the accelerometer data
    accel = ('X: ' + str(x) + '; Y: ' + str(y) + '; Z: ' + str(z))

# Writes the time, altitude, and accelerometer string to the document
    f.seek(0,2)
    f.write('T+ ' + str(T) + '\n')
    f.write('     A+ ' + str(a) + 'm\n')
    f.write('     ' + str(accel) + '\n')

# If the elapsed time is a multiple of the autosave interval
    if elapsed != 0:
        if elapsed % int(autosave) == 0:
            f.close() #                               Closes (saves) document
            f = open(str(txt),'r+') # Re-opens document
