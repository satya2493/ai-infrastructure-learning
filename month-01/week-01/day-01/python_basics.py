# Day 1: Python Networking Calculations
# Spine-Leaf Calculator

#1. Create a dictionary representing a spine switch
spine_switch = {
    "hostname": "SPINE-01",
    "model": "Arista DCS-720",
    "ports": 48,
    "uplink_speed": "400G",
    "role": "spine"
}

#2. Create a list of 4 leaf switches
leaf_switches = [
    {"hostname": "LEAF-01", "model": "Arista DCS-705", "ports": 48, "connected_servers": 40 },
    {"hostname": "LEAF-02", "model": "Arista DCS-705", "ports": 48, "connected_servers": 38 },
    {"hostname": "LEAF-03", "model": "Arista DCS-705", "ports": 48, "connected_servers": 42 },
    {"hostname": "LEAF-04", "model": "Arista DCS-705", "ports": 48, "connected_servers": 36 }
]

#3. Write a function that calculates the total number of servers in the fabric
def calculate_total_servers (leaf_list):
    total_servers = 0
    for leaf in leaf_list:
        total_servers = total_servers + leaf["connected_servers"]
    return total_servers

#4. Write a function that calculates the oversubscription ration
# Each leaf has 48x10G downlink (480 Gbps), 6x40G uplink (240 Gbps)
def calculate_oversubscription():
    downlink = 48 * 10
    uplink = 6 * 40
    ratio = downlink/uplink
    return ratio

#5. Print results
print("=" * 60)
print(f"Spine Switch: {spine_switch['hostname']}")
print(f"Number of Leaf Switches: {len(leaf_switches)}")
print(f"Total Servers: {calculate_total_servers(leaf_switches)}")
print(f"Oversubscription Ratio: {calculate_oversubscription()}:1")
print("=" * 60)



