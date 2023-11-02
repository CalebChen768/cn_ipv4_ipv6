import yaml

# Load the data file
with open('data.txt', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

# Separate the IPv4 and IPv6 addresses
ipv4_addresses = [item for item in data['payload'] if ':' not in item]
ipv6_addresses = [item for item in data['payload'] if ':' in item]

# Prepare the data for output
ipv4_data = {'payload': ipv4_addresses}
ipv6_data = {'payload': ipv6_addresses}

# Write the addresses to separate files
with open('ipv4.txt', 'w') as file:
    yaml.dump(ipv4_data, file)

with open('ipv6.txt', 'w') as file:
    yaml.dump(ipv6_data, file)
