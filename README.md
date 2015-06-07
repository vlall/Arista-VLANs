# Arista-Learn
Learning commands for Arista VLAN configuration
##FAQ
#####How do you create a VLAN:

`switch(config)#vlan 45`

`switch(config-vlan-45)#`
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



**Example**:
 This command displays status and ports of VLANs 1-1000.
 
`switch>show vlan 1-1000`

|VLAN |Name |  Status | Ports|
| ------------- |------|-------| ----|
|1  |  default   | active | Po1  |
|184 |fet.arka |  active| Cpu, Po1, Po2|
|262 |mgq.net | active |PPo2, Po1|
|512 |sant.test | active | Cpu, Et16, Po1|
|821 |ipv6.net |  active |  Cpu, Po1, Po7|
