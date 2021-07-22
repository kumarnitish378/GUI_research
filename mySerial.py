import serial
import time
import sys

ser = None


def configure_port(port, baudrate):
    try:
        global ser
        ser = serial.Serial()
        ser.port = port
        ser.baudrate = baudrate
        ser.bytesize = serial.EIGHTBITS
        ser.parity = serial.PARITY_NONE
        ser.stopbits = serial.STOPBITS_ONE
        ser.timeout = 2.0
        ser.xonxoff = False
        ser.rtscts = False
        ser.dsrdtr = False
        ser.writeTimeout = 2
        print("serial port configuration done")
    except Exception as e:
        print(str(e))


def open_port():
    try:
        ser.open()
        print("serial port opened successfully")
    except Exception as e:
        print(str(e))


def available_bytes():  # doesn't run on windows !!
    version = sys.version[0]
    print('current version', version)
    if int(sys.version[0]) < 3:
        return ser.in_waiting
    else:
        return ser.inWaiting


def read_all_bytes():
    data = []
    while ser.in_waiting:
        data.append(ser.read(1))
    return data


def read_n_bytes(n):
    data = []
    if ser.in_waiting:
        time.sleep(0.1)
        while (n > 0):
            data.append(ser.read(1))
            n = n - 1
        return data
    return data


def read_serial_readline(n=None):
    """
    io.IOBase.readline()
    """
    if n is None:
        return ser.readline()
    else:
        return ser.readline(n)


def clear_buffer():
    ser.reset_input_buffer()
    ser.reset_output_buffer()


def close_serial_port():
    ser.close()
    print('closed')


def serial_write(r=None):
    ser.write(r.encode('utf-8'))
    # print(r)


if __name__ == '__main__':
    # configure_port('COM3', 115200)
    # open_port()
    pass
    # print('running as main thread')
    # while True:
    #     try:
    #         # time.sleep(0.1)
    #         # print(available_bytes())
    #         # print(read_n_bytes(2))
    #         print(read_serial_readline())
    #         # clear_buffer()
    #         # time.sleep(2)
    #     #         print(read_all_bytes())
    #     except KeyboardInterrupt as e:
    #         print(str(e))
    #         close_serial_port()