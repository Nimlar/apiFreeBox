#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This example can be run safely as it won't change anything in your box configuration
'''

from freepybox import freepybox


# Instantiate Freepybox class using default application descriptor 
# and default token_file location
fbx = freepybox()

# Connect to the freebox with default http protocol
# and default port 80
# Be ready to authorize the application on the Freebox if you use this
# example for the first time
fbx.open('mafreebox.freebox.fr')

# Dump freebox configuration using system API
# Extract temperature and mac address
fbx_config = fbx.system.get_config()
print('Freebox temperature : {0}'.format(fbx_config['temp_sw']))
print('Freebox mac address : {0}'.format(fbx_config['mac']))

# Dump DHCP configuration using dhcp API
fbx_dhcp_config = fbx.dhcp.get_config()
# Modify ip_range configuration
#fbx_dhcp_config['ip_range_start'] = '192.168.0.10'
#fbx_dhcp_config['ip_range_end'] = '192.168.0.50'
# Send new configuration to the freebox. This line is commented to avoid any disaster.
# fbx.dhcp.set_config(fbx_dhcp_config)

# Get the call list and print the last call entry
fbx_call_list = fbx.call.get_call_list()
print(fbx_call_list[0])


print('Freebox player list: {0}'.format(fbx_config['mac']))

# Reboot your freebox. This line is commented to avoid any disaster.
# fbx.system.reboot()

# Close the freebox session
fbx.close()

