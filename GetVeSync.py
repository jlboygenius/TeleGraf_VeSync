#!/usr/bin/python
from pyvesync.vesync import VeSync
import json



Outlets = []




manager = VeSync("USER_EMAIL", "PASSWORD")
manager.login()
manager.update()

# Get electricity metrics of devices
#print manager.devices[0].device_name
for switch in manager.devices:
    #print("Switch %s is currently using %s watts" % (switch.device_name, switch.get_power()))
    #print("It has used %skWh of electricity today" % (switch.get_kwh_today()))
    #print(switch.device_status)
    #print(switch.device_type)
    #device = Outlet()
    #device.DeviceName = switch.device_name
    #Outlets.append(device)
    x = {
     "name":"VeSync",
     "DeviceName":switch.device_name,
     "State":switch.device_status,
     "CurrentPower":switch.get_power(),
     "Type":switch.device_type,
     "TodayPower":switch.get_kwh_today(),
     "ConnectionStatus":switch.connection_status,
     "DeviceStatus":switch.device_status
    }
    Outlets.append(x)



print(json.dumps(Outlets))
