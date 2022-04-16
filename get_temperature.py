from dth import DTH
import time
from machine import Pin

def GetSpeedofSound(Temp):
    SoS = (331.3 * (1 + (Temp/273.15))/10000)
    #print(str(SoS))
    return SoS



def GetTemp():
    th = DTH(Pin('P3', mode=Pin.OPEN_DRAIN),1)
    time.sleep(2)
    result = th.read()
    return result.temperature
