import yaml

# Load the data file
with open('data.txt', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

# Separate the IPv4 and IPv6 addresses
ipv4_addresses = [item for item in data['payload'] if ':' not in item]
ipv6_addresses = [item for item in data['payload'] if ':' in item]

# Write the addresses to separate files
with open('ipv4.txt', 'w') as file:
    for address in ipv4_addresses:
        file.write(f"{address}\n")

with open('ipv6.txt', 'w') as file:
    for address in ipv6_addresses:
        file.write(f"{address}\n")
