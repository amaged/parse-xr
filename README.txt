parsexr
=======

Parsing IOS-XR Running Configuration.

Provide running-configuration as input (STDIN) to the script and it prints the count of interfaces and features/components configured.

Example:

apogee:cat amaged$ python parsexr.py < running-config.txt 
All interfaces 28163
ipv4 addresses 16297
ipv6 addresses 5647
interface_bundle_counter 147
interface_giga_counter 17431
interface_ten_gig_counter 1193
Interface serial counter 7614
interface sub counter 22651
interface without dot 5235
interface with l2transport 0
interface_without_l2transport 23732
snmp_trap_counter 33
bundle_with_l2transport 147
spanning_tree_mst_counter 2
spanning_tree_mstag_counter 0
an_port_circuitid_counter 2
bridge_group_counter 3
bridge_domain_counter 2056
vf_pw_counter 0
pbb_core_bd_counter 24
pbb_edge_bd_counter 4
ethernet_ring_g8032_counter 1
xconnect_groups_counter 3
xconnect_p2p_counter 654
p2p_neigh_counter 654
bridge_domain_counter 2056
bridge_neighbor_counter 2000

