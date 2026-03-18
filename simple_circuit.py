from skidl import Net, Part, generate_netlist

# Create a voltage source (5V)
vcc = Part('Device', 'V', value='5V')

# Create a resistor (1k Ohm)
r1 = Part('Device', 'R', value='1k')

# Create ground
gnd = Part('Device', 'GND')

# Connect voltage source to resistor and ground
net_vcc = Net('VCC')
net_vcc += vcc[1], r1[1]

net_gnd = Net('GND')
net_gnd += vcc[2], r1[2], gnd[1]

# Generate netlist
generate_netlist()
