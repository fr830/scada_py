from pymodbus.client.sync import ModbusTcpClient


def write(c):
    c.write_coil(1, False)
    c.read_coils(1, 1)

if __name__ == "__main__":
    import timeit
    client = ModbusTcpClient('127.0.0.1', 5020)
    client.connect()
    print (timeit.timeit("lamda:write(client)", setup="from __main__ import write"))
    client.close()
