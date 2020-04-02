from PyAccessPoint import pyaccesspoint
import logging
import time
from wireless import Wireless 

# logging.basicConfig(
#     #filename= 'queuetest.log',
#     level=logging.DEBUG,
#     format='%(asctime)s  line %(lineno)d  [%(levelname)s]'+\
#         '(%(threadName)-12s) %(message)s',)

# time.sleep(1)

# access_point = pyaccesspoint.AccessPoint(
#             # ip='192.168.45.1',
#             # netmask='255.255.255.0',
#             # ssid='thingsintouch',
#             # password='1111'
#             )
# access_point.start()

# time.sleep(20)

# access_point.stop()

wireless = Wireless()

print('current: ',wireless.current())
print('interface: ',  wireless.interface())
print('driver: ', wireless.driver())
print('interfaces: ', wireless.interfaces())


#wireless.connect(ssid='Tech_D0047892', password='UVKZDTEJ') 