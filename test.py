import requests
import time
while True:
    r=requests.post("https://discord.com/api/v9/guilds/1211384349107167372/roles", headers={"Authorization":"-I.zI3IqQjRTnoGKrdGrgOHMNfdrxXboFew5sQPAc"}, data={"name":"pene", "permissions":"0", "color":"0"})
    time.sleep(0.5)
print(r.status_code)