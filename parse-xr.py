import sys, re

# Author : Ahmed Maged
# amaged@gmail.com

#
# Defining the counters
#

vrf_counter = 0
snmp_trap_counter = 0
spanning_tree_mst_counter = 0
spanning_tree_mstag_counter = 0
an_port_circuitid_counter = 0
bridge_group_counter = 0
bridge_domain_counter = 0
vf_pw_counter = 0
pbb_core_bd_counter = 0
pbb_edge_bd_counter = 0
ethernet_ring_g8032_counter = 0
xconnect_groups_counter = 0
xconnect_p2p_counter = 0
xconnect_pw_counter = 0
p2p_neigh_counter = 0
bridge_neighbor_counter = 0

interface_counter = 0
ipv6_counter = 0
ipv4_counter = 0
interface_giga_counter = 0
interface_ten_gig_counter = 0
interface_bundle_counter = 0
interface_serial_counter = 0
interface_sub_counter = 0
interface_without_dot = 0
interface_with_l2transport = 0
interface_without_l2transport = 0
bundle_with_l2transport = 0
pbb_edge_counter = 0

#
# General default state is unknown 
# Other states possible : interface or bgp or ospf...etc
#

current_state = "unknown"
l2vpn_state = ""

#
# Enter a loop that takes input from the STDIN
#

for line in sys.stdin:
#
# Split the line into words, separator is a space and put result in a list
#
	if current_state == 'l2vpn':
		if re.match("^!$", line):
				current_state = "unknown"
		elif l2vpn_state == "p2p":
			if re.match("^  !$", line):
				l2vpn_state = None
			elif 'neighbor' in line:
				p2p_neigh_counter += 1
		else:
			if 'p2p' in line:
				xconnect_p2p_counter += 1
				l2vpn_state = "p2p"
			elif 'neighbor' in line:
				bridge_neighbor_counter += 1
			elif 'bridge-domain' in line:
				bridge_domain_counter += 1
	elif current_state == 'interface':
		if re.match("^!$", line):
			current_state = "unknown"
		elif 'ipv6 address' in line:
			ipv6_counter += 1
		elif 'ipv4 address' in line:
			ipv4_counter += 1
	else:
		# if the first word is 'interface' then we switch the state to interface 
		if re.match("^interface", line):
			interface_counter += 1
			current_state = 'interface'
			try:
				# Use Regex to match interface type and add it to a list then filter
				interface_type = re.findall("[A-Z][a-z\|A-Z]+", line)[0]
				if interface_type == "GigabitEthernet":
					interface_giga_counter += 1
				elif interface_type == "TenGigE":
					interface_ten_gig_counter += 1
				elif interface_type == "Bundle":
					if 'l2transport' in line:
						bundle_with_l2transport += 1
						interface_bundle_counter += 1
				elif interface_type == "Serial":
						interface_serial_counter += 1
				if '.' in line:
					interface_sub_counter += 1
				else:
					interface_without_dot += 1
				if 'point-to-point' in line:
					p2p_int_counter += 1
				#if 'l2transport' in line:
				#	interface_with_l2transport += 1
				else:
					interface_without_l2transport += 1
			except:
				pass
		elif re.match("^l2vpn", line):
			current_state = "l2vpn"
		elif re.match("^snmp-server traps", line):
			snmp_trap_counter += 1
		elif re.match("^vrf", line):
			vrf_counter += 1 
		elif re.match("spanning-tree mst", line):
			spanning_tree_mst_counter += 1
		elif re.match("spanning-tree mstag", line):
			spanning_tree_mstag_counter += 1
		elif re.match("^ an-port circuit-id", line):
			an_port_circuitid_counter += 1
		elif re.match("^ bridge group", line):
			bridge_group_counter += 1
		elif re.match("^  bridge-domain", line):
			bridge_domain_counter += 1
		elif re.match("^   vfi", line):
			vf_pw_counter += 1
		elif re.match("^   pbb core", line):
			pbb_core_bd_counter += 1
		elif re.match("^   pbb edge", line):
			pbb_edge_bd_counter += 1
		elif re.match("^ ethernet ring g8032", line):
			ethernet_ring_g8032_counter +=1 
		elif re.match("^ xconnect group", line):
			xconnect_groups_counter += 1
		elif re.match("^  p2p", line):
			xconnect_p2p_counter += 1


print("interfaces %d" % (interface_counter))
print("ipv4 %d" % (ipv4_counter))
print("ipv6 %d" % (ipv6_counter))
print("interface_bundle_counter %d" % (interface_bundle_counter))
print("interface_giga_counter %d" % (interface_giga_counter))
print("interface_ten_gig_counter %d" % (interface_ten_gig_counter))
print("Interface serial counter %d" % (interface_serial_counter))
print("interface sub counter %d" % (interface_sub_counter))
print("interface without dot %d" % (interface_without_dot))
print("interface with l2transport %d" % (interface_with_l2transport))
print("interface_without_l2transport %d" % (interface_without_l2transport))
print("snmp_trap_counter %d" % (snmp_trap_counter))
print("bundle_with_l2transport %d" % (bundle_with_l2transport))
print("spanning_tree_mst_counter %d" % (spanning_tree_mst_counter))
print("spanning_tree_mstag_counter %d" % (spanning_tree_mstag_counter))
print("an_port_circuitid_counter %d" % (an_port_circuitid_counter))
print("bridge_group_counter %d" % (bridge_group_counter))
print("bridge_domain_counter %d" % (bridge_domain_counter))
print("vf_pw_counter %d" % (vf_pw_counter))
print("pbb_core_bd_counter %d" % (pbb_core_bd_counter))
print("pbb_edge_bd_counter %d" % (pbb_edge_bd_counter))
print("ethernet_ring_g8032_counter %d" % (ethernet_ring_g8032_counter))
print("xconnect_groups_counter %d" % (xconnect_groups_counter))
#print("xconnect_p2p_counter %d" % (xconnect_p2p_counter))
#print("xconnect_pw_counter %d" % (xconnect_pw_counter))

print("xconnect_p2p_counter %d" % (xconnect_p2p_counter))
print("p2p_neigh_counter %d" % (p2p_neigh_counter))
print("bridge_domain_counter %d" % (bridge_domain_counter))
print("bridge_neighbor_counter %d" % (bridge_neighbor_counter))
