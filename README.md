# Arista-Learn
Learning commands for Arista VLAN configuration
##FAQ
#####How do you create a VLAN:
```
switch(config)#vlan 45
switch(config-vlan-45)#
```
- The default name for VLAN 45 Is VLAN0045

#####How do you view all VLANs?
  `show VLAN`
  Shows all VLANs

`show vlan [VLAN_LIST] [PORT_ACTIVITY]`


|               |      VLAN_LIST      | PORT_ACTIVITY  |
| ------------- |:-------------:| -----:|
| `show VLAN`   | All | n/a |
| `show VLAN 40-60`| 40-60| n/a| 
| `show VLAN active-configuration`     | All      |   active |
|  `show VLAN configured-ports` |   All    |   active/inactive |



**e.g.**
 This command displays status and ports of VLANs 1-1000.
 
`switch>show vlan 1-1000`

|VLAN |Name |  Status | Ports|
| ------------- |------|-------| ----|
|1  |  default   | active | Po1  |
|184 |fet.arka |  active| Cpu, Po1, Po2|
|262 |mgq.net | active |PPo2, Po1|
|512 |sant.test | active | Cpu, Et16, Po1|
|821 |ipv6.net |  active |  Cpu, Po1, Po7|


#####Other VLAN commands

|       Command        |      Description      |
| ------------- |:-------------:| -----:|
| `>show vlan dynamic`   | displays the source and quantity of dynamic VLANs on the switch. |
| `>show vlan internal allocation policy` | the list of VLANs that are allocated to routed ports along with the direction by which VLANs are allocated | 
| `>show vlan internal usage`     |   displays the VLANs that are allocated to routed ports.    | 
|  `>show vlan private-vlan` |   lists the VLAN type and attached ports configuration of the private VLANs    |  
|  `>show vlan summary` |   Returns number of VLANs on this switch    |  
|`>show vlan [VLAN_LIST`] trunk group' | displays the trunk group membership of all configured VLANs|

#####How do I change VLAN transmission state?
`state active` | allows traffic
`state suspend` | blocks traffic

```
switch(config)#vlan 100-102
switch(config-vlan-100-102)#state suspend
switch(config-vlan-100-102)#
```
#####What is switchport mode?

There are 5 switching modes:
Mode| Description  
----|------------------
access    |
trunk     |
dot1q-tunnel|
tap     |
tool |

You can restore switchport modes by using
`>default switchport mode` 
