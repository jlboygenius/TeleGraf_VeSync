# TeleGraf_VeSync
Input plugin for Telegraf to import Power usage and Outlet status data from VeSync API

Etekcity outlets on amazon can track power usage. They are sold under various names, but use the VeSync app to control the outlets. 
https://www.amazon.com/Etekcity-Voltson-Outlet-Monitoring-Required/dp/B074GVPYPY






Telegraf Config file input:
Add the following to your telegraf.conf file (/etc/telegraf/telegraf.conf)


#veSync monitoring
[[inputs.exec]]
    commands = ["/home/pi/GetVeSync.py"]
    timeout = "20s"
    data_format = "json"
    name_suffix = ""
    json_name_key = "name"
    tag_keys = ["DeviceName","Type"]

