# Day 1: Python Setup Test
# My AI Infrastructure Learning Journey

print("🚀 Python is working!")
print("=" * 50)

# Basic spine-leaf calculation
spine_count = 4
leaf_count = 20
servers_per_leaf = 48

total_servers = leaf_count * servers_per_leaf
connections = leaf_count * spine_count

print(f"Data Center Fabric Configuration:")
print(f"  Spine Switches: {spine_count}")
print(f"  Leaf Switches: {leaf_count}")
print(f"  Servers per Leaf: {servers_per_leaf}")
print(f"  Total Servers: {total_servers}")
print(f"  Total Spine-Leaf Connections: {connections}")
print("=" * 50)

# Calculate oversubscription ratio
# Each leaf: 48x 10G downlinks, 6x 40G uplinks
downlink_capacity = 48 * 10  # Gbps
uplink_capacity = 6 * 40     # Gbps
oversubscription = downlink_capacity / uplink_capacity

print(f"\nOversubscription Ratio: {oversubscription}:1")

if oversubscription <= 3:
    print("✅ Good oversubscription ratio!")
else:
    print("⚠️  High oversubscription - consider adding uplinks")