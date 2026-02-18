# Exercise: Build a network inventory tracker

# PART 1: Create data structures
spine_switches = [
    {"hostname": "SPINE-01", "vendor": "Arista", "uptime_days": 120},
    {"hostname": "SPINE-02", "vendor": "Arista", "uptime_days": 95}
]

leaf_switches = [
    {"hostname": "LEAF-01", "vendor": "Cisco", "uptime_days": 200},
    {"hostname": "LEAF-02", "vendor": "Cisco", "uptime_days": 180},
    {"hostname": "LEAF-03", "vendor": "Arista", "uptime_days": 45}
]

# PART 2: Write these functions

def count_switches_by_vendor(switch_list, vendor_name):
    vendor_count = 0
    for switch in switch_list:
        if switch["vendor"] == vendor_name:
            vendor_count = vendor_count + 1
    return vendor_count

def find_switches_needing_reboot(switch_list, max_uptime):
    switches_needing_reboot = []
    for switch in switch_list:
        if switch["uptime_days"] > max_uptime:
            switches_needing_reboot.append(switch["hostname"])
    return switches_needing_reboot

def calculate_average_uptime(switch_list):
    total_uptime = 0
    for switch in switch_list:
        total_uptime = total_uptime + switch["uptime_days"]
    number_of_switches = len(switch_list)
    average_uptime = total_uptime/number_of_switches
    return average_uptime


# PART 3: Test your functions
print("=" * 60)
print(f"Cisco leaf switches: {count_switches_by_vendor(leaf_switches, 'Cisco')}")
print(f"Arista leaf switches: {count_switches_by_vendor(leaf_switches, 'Arista')}")
print(f"Switches needing reboot: {find_switches_needing_reboot(spine_switches, 100)}")
print(f"Average leaf uptime: {calculate_average_uptime(leaf_switches):.1f} days")
print("=" * 60)
