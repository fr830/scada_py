from pymodbus.client.sync import ModbusTcpClient
import timeit

client = ModbusTcpClient('127.0.0.1', 5020)
client.connect()
def write(c):
   c.write_coil(1, False)
   c.read_coils(1,1)
print timeit.timeit(lambda:write(client), number=100)

#result = client.read_coils(1,1)
#print result.bits[0]
client.close()
