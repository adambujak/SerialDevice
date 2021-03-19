import os
import time
import serial
from threading import Thread, Lock

class SerialDevice:
    def __init__(self, serialPort, baudRate=115200, readSleepTimeMs=1):
        self.serialMutex = Lock()
        self.readSleepTime = readSleepTimeMs / 1000;
        self.serialInstance = serial.Serial(serialPort, baudRate, timeout=0.5)
        self.readThreadInstance = Thread(target=self.read_thread, args=[])
        self.readThreadInstance.start()

    def read_thread(self):
        while 1:
            readData = self.read_raw_char()
            if readData != '': #empty bytes
                self.read_callback(readData)
            time.sleep(self.readSleepTime)

    def write_bytes(self, byteData):
        self.serialMutex.acquire()
        self.serialInstance.write(byteData)
        self.serialMutex.release()

    def write_string(self, string):
        self.write_bytes(string.encode('ascii'))

    def read_line(self):
        self.serialMutex.acquire()
        retval = None
        try:
            retval = self.serialInstance.readline().decode('ascii')
        except UnicodeDecodeError:
            pass
        self.serialMutex.release()
        return retval

    def read_raw_line(self):
        self.serialMutex.acquire()
        retval = self.serialInstance.readline()
        self.serialMutex.release()
        return retval

    def read_raw_char(self):
        self.serialMutex.acquire()
        readval = self.serialInstance.read(1)
        self.serialMutex.release()
        return readval

    def read_callback(self):
        # User should overwrite this in their own class
        pass
