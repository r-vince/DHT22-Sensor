import get_temperature

from dth import DTH

temp = get_temperature.GetTemp()
humid = get_temperature.GetHumidity()
SOS = get_temperature.GetSpeedofSound(temp)

print(temp)
print(humid)
print(SOS)
