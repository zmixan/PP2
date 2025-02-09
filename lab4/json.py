import json
with open("sample-data.json", "r") as f:
    data = json.load(f)
print("Interface Status")
print("=" * 86)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 50, "-" * 20, "-" * 7, "-" * 6)
for item in data["imdata"]:  
    dn = item["l1PhysIf"]["attributes"]["dn"]
    desc = item["l1PhysIf"]["attributes"]["descr"]
    speed = item["l1PhysIf"]["attributes"]["speed"]
    mtu = item["l1PhysIf"]["attributes"]["mtu"]
    
    print(f"{dn:<50} {desc:<20} {speed:<8} {mtu:<6}")
