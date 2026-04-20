
### Network

- network is a group of devices connected together to share data, resources and applications.

- can connect via cable or Wi-Fi.

#### Common Types of Network ( BY Geographical Area)

1. ***PAN (Personal Area Network**)* : is the smallest type, covering a few meters, typically used for personal devices like Bluetooth headphones, phones and tablets.

2. ***LAN ( Local Area Network)***: covers a small, specific area like a home, office, or single building. These are high speed and privately managed.

3. ***WLAN ( Wireless Local Area Network)*** : a LAN that uses wireless technology, such as Wi-Fi, to connect devices within a limited area.

4. ***CAN (Campus Area Network)*** : larger than LAN but smaller than MAN, linking multiple LANs within a specific geographic area like university campus or military base.

5. ***MAN (Metropolitan Area Network)***: spans a larger area, typically a city or town, connecting multiple LANs together.

6. ***WAN ( Wide Area Network) or Internet*** : covers large, broad geographical areas such as countries, continents, or the entire globe.

#### Network Devices

-  **Switch** : connects multiple devices inside the same network(LAN) and helps to communicate.
		It sends data only to the correct device
		It keeps communication inside the LAN

- **Router** : a device that connects different networks together.
	-It directs traffic between networks
	-decides where data should go

- **Modem** : connect router to internet service provider(ISP).
	-converts signal from ISP to Internet signals

### IP Address
- is a unique number that identifies a device in a network.
- IP = internet protocol
- is used for : sending data to the correct device
			-identifying sender and receiver
			- routing traffic across network

#### Public IP vs Privet IP

- ==Not all devices can be directly visible on the internet==. So we use Private and public IP addresses.

| Private IP                                      | Public IP                                       |
| ----------------------------------------------- | ----------------------------------------------- |
| - used inside LAN                               | - is visible on the internet                    |
| - can not be reached directly from the internet | - assigned by ISP, used by websites and servers |
| - common ranges : 192.168.x.x -- 10.x.x.x       | - are unique world wide                         |
|                                                 | -internet uses public IPs to find networks      |

#### MAC Address
- is unique ==physical address== assigned to a network device.
- MAC = media access control
- is tied to the network hardware.
- usually ==does not change==.
- It consists letters and numbers separated by colons.
- Used for identifying devices in side a local network
	  - used by switches to send data correctly

| IP Address          | MAC Address      |
| ------------------- | ---------------- |
| Logical address     | physical address |
| can change          | usually fixed    |
| used across network | used inside LAN  |
**DNS (Domain Name System)** : a system that converts domain names into IP addresses.
	E.g.: google.com   to IP address


## IPv4 class ranges


| class | range   |
| ----- | ------- |
| A     | 1-127   |
| B     | 188-191 |
| C     | 192-223 |
| D     | 224-239 |
| E     | 240-255 |
127.0.0.1 : for localhost
0.x.x.x: Reserved 

## Private IP Ranges

These are special private ranges:

- Class A private: **10.0.0.0 – 10.255.255.255**
- Class B private: **172.16.0.0 – 172.31.255.255**
- Class C private: **192.168.0.0 – 192.168.255.255**


