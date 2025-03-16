import json 


print("Interface status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

<<<<<<< HEAD:labs/lab4/json/ex.py
with open('D:\PP2\labs\lab4\json\sample-data.json') as f:
=======
with open('json/sample-data.json') as f:
>>>>>>> 6b0daea7c69d8f6dd74f7293727203d33daf29d6:lab4/json/ex.py
    data = json.load(f)

request_from_server = data["imdata"][0]["l1PhysIf"]["attributes"]["dn"]
speed = data["imdata"][0]["l1PhysIf"]["attributes"]["fecMode"]
mtu = data["imdata"][0]["l1PhysIf"]["attributes"]["mtu"]
print(request_from_server, "                            ", speed," ", mtu )
print(request_from_server, "                            ", speed," ", mtu )
print(request_from_server, "                            ", speed," ", mtu )