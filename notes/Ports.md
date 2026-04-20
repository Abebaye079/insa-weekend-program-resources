- Ports are logical endpoints on a computer used by services.
- IP = identifies the machine
- Port = identifies the service on that machine

E.g., 192.168.1.10:80  = web server

### Port Ranges

- 0-1023 --> well known ports
- 1024-49151 --> Registered
- 49152-65535  --> Dynamic/private

### Well Known Ports + Attacks

| Port    | Service | Risk Level | Common Attacks                                                                                                          | Key Attack            |
| ------- | ------- | ---------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------- |
| 21      | FTP     | High       | - Brute force login   -Anonymous login               - Sniffing credentials ( plain text)                               | Sniffing, brute force |
| 22      | SSH     | Medium     | - Brute force attack               - Credential stuffing             - Key based attacks (if misconfigured)             | Brute force           |
| 23      | Telnet  | High       | -Password sniffing                 - Man in the Middle              -Brute force                                        | MITM, sniffing        |
| 25      | SMTP    | Medium     | -Email spoofing                    -Spam relay (open relay abuse)                                    - phishing attacks | Spoofing              |
| 53      | DNS     | High       | -DNS spoofing / Poisoning    - DNS amplification (DDoS)  - cache poisoning                                              | Poisoning             |
| 80      | HTTP    | High       | -Man in the Middle                - Session hijacking                - XSS (cross site scripting)     -SQL injection    | XSS, MITM             |
| 443     | HTTPS   | Medium     | - SSL/TLS attacks<br>- Certificate spoofing<br>- Downgrade attacks<br>- Still vulnerable to XSS / SQL injection         | TLS attacks           |
| 139/445 | SMB     | Critical   | - EternalBlue exploit (used in WannaCry ransomware attack)<br>- Null session attack<br>- SMB relay attack               | EternalBlue           |
| 3389    | RDP     | Critical   | - Brute force<br>- BlueKeep exploit<br>- Session hijacking                                                              | Brute force           |


# Attacks

### 1. Brute Force Attack

- is trying or guessing many usernames/ password combinations until one works.

- Attackers use tools to guess passwords automatically like: Hydra, Medusa.

#### - Hydra 
- is password cracking tool to guess login credentials on different network services.
- uses methods like Brute-force / dictionary attack

#### - Medusa
- Hydra and Medusa do almost the same job, but Medusa is often preferred for **clean parallel attacks**, while Hydra is more popular and widely used.
	
	- Parallel attack means doing many login attempts at the same time, instead of one by one.
		- It is much faster attacks
		- saves times
		- can overwhelm weak servers


### 2. Man-in-the-Middle (MITM)

- is secretly intercepting communication between two parties.
- How it happens: Fake Wi-Fi , ARP spoofing

#### - Using Fake Wi-Fi 
- attackers create fake wi-fi network that looks real , then u will connect.
- Steps:     1. Creates fake hotspot  : same name as real Wi-Fi
	       2. Device connects automatically, since it has strong signal usually devices connect to it.
	       3. Attacker becomes the "router" : You -> Attacker -> Internet
	       4. Attacker intercepts traffic: can see the data if not encrypted, modify requests, redirect to fake websites

#### -Using ARP Spoofing
##### - ARP (Address Resolution Protocol) 
- is used to find MAC address from an IP address.
- It works by asking everyone on the network who has this IP
- Has no security, any device can reply to ARP request 
-  <u> How it works </u> 
	- your computer with IP 192.168.1.10 wants to send data to router with IP 192.168.1.1. But does not know the MAC address so the PC sends message to everyone on the network "who has 192.168.1.1", this is called ARP request. Then the router replies " I am 192.168.1.1, my MAC is AA:BB:CC:DD". Communication starts
- So attacker might send fake ARP message, then the traffic rerouted. Normally You ->Router, but then You -> Attacker -> Router


### 3. Sniffing ( Packet Sniffing)

- is capturing and reading network data.
- It works because some protocols send data in plain text (no encryption)
- used tools like Wireshark, tcpdump

#### - Wireshark
- is network analysis tool used to capture and inspect network traffic( packets).
 - What it does 
	- Listens to your network
	- Captures data packets going in and out
	- Shows what’s inside those packets in readable form
#### - tcpdump
- is command line network packet capture tool.
- What it does (simple)
	- Captures packets from a network interface
	- Displays them in real time in the terminal
	- Lets you filter specific traffic (IP, port, protocol)
	E.g., `tcpdump -i eth0` : capture all traffic on interface eth0
		`tcpdump port 80` : captures only HTTP traffic
- It is very fast and efficient, works on servers ( no GUI needed), strong filtering options


### 4. SQL Injection (SQLi)

- is injecting malicious SQL code into a website to access database data.
- is tricking database using malicious input.

### 5. Cross-Site Scripting (XSS)

- is injecting malicious JavaScript into a website to attack users.
- Has two types stored XXS and reflected XXS
- #### Stored XXS
	- the malicious script is saved on the server/database and attacks everyone who visits.
#### Reflected XSS (Non-Persistent)
- the script is not saved, it is reflected immediately in the response.
- Attackers create malicious link and sent to victim  via email or phishing message, then the server reflects input in response, the script runs victim's browser.
- It needs users interaction

| Brute Force   | Guess password             |
| ------------- | -------------------------- |
| MITM          | Intercept communication    |
| sniffing      | Capture network data       |
| SQL Injection | Attack database via input  |
| XSS           | inject malicious JavaScipt |

### 6. DNS Poisoning ( DNS Cache Poisoning)

- is modifying DNS records to redirect users to malicious site.
-  How it works:
1. User wants to visit `bank.com`
2. Computer asks DNS server: “What’s the IP of bank.com?”
3. Attacker spoofs the response: “IP = attacker’s server”
4. User ends up on fake website controlled by attacker
- Results: phishing attacks, stealing credentials, malware distribution 


### 7. DNS Amplification (DDOS)

- Attacker overwhelms a target using DNS server as a "force multiplier".
-  How it works:
1. Attacker sends **small DNS request** with **spoofed victim IP**
2. DNS server replies **large response** to victim
3. Repeat thousands of times → victim gets **flooded**
- It results network downtime, denial of service.


### 8. Kerberoasting

- is abusing Kerberos tickets in Windows Active Directory to crack passwords.
- Kerberoasting = steal encrypted service tickets → crack password offline
-  How it works:
1. Attacker requests **service tickets** for users
2. Tickets are **encrypted using user’s password hash**
3. Attacker captures tickets and **cracks them offline**
- It results in gaining domain admin credentials, can pivot through entire Windows network.



