# Custom Component for NeoSmartBlinds Integration on Home Assistant

The NeoSmartBlinds platform allows you to control a NeoSmartBlind / group of NeoSmartBlinds via a NeoSmartBlinds controller.

There is currently support for the following device types within Home Assistant:

-   Cover

## Installation

To begin with it is recommended you ensure your NeoSmartBlinds controller has a static IP addresses, you may need to configure this via your routers DHCP options.

Download the custom component in to your folder <config_directory>/custom_components/neosmartblinds

# Cover Configuration 

### Example of basic configuration.yaml
```
cover:
  - platform: neosmartblinds
    name: Blind One
    host: 192.168.0.13
    blind_code: 021.230-04-
    close_time: 65
```

## Configuration variables

cover:

**platform** (string)(Required) 
Must be set to neosmartblinds

**host** _(string)(Required)_
The IP of the NeoSmartBlinds controller, e.g., 192.168.0.10.

**name** _(string)(Required)_
The name you would like to give to the NeoSmartBlind.

**blind_code** _(string)(Required)_
The blind code. - this is available from the NeoSmartBlind app

**close_time** _(string)(Required)_
Time taken in seconds to close this blind (use a stop watch to measure)


## Supported features

**Open**
Up

**Close**
Down

**Tilt-Up**
Micro-Up

**Tilt-Down**
Micro-Down

**Set-Position & Favourite Position** - please note this is calculated using the close_time

Setting the position: 
**<= 49** will move the blind down, this means set position 25, moves the blind down and stops after 25% of your close_time
**>=51** will move the blind up, this means set position 75, moves the blind up and stops after 25% of your close_time
**==50** will set your blind to its stored favourite position 
