# Copyright 2017 Servers.com
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from networking_generic_switch.devices import netmiko_devices


class BrocadeFastIron(netmiko_devices.NetmikoSwitch):
        ADD_NETWORK = (
            'vlan {segmentation_id} by port',
            'name {network_id}',
        )

        DELETE_NETWORK = (
            'sh ip',  # UGLY but we don't want to remove vlan, and need (?) to send something
        )

        PLUG_PORT_TO_NETWORK = (
			'vlan {segmentation_id} by port',
            'untagged ether {port}',
        )

        DELETE_PORT = (
			'vlan {segmentation_id} by port',
            'no untagged ether {port}',
        )
