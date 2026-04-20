 Nmap (“Network Mapper”) is an open source tool for network exploration and security auditing

### Used for:

- Networking scanning : to find all devices on a network
- Port scanning : to check which ports are open
- To detect what software is running on open ports
- To guess OS of a target
- to find what type of packet filters/firewalls are in use
- to find vulnerabilities

-**PORT** : is gateway on a computer. Each port has a number. (0-65535)

-**SERVICE** : is a program running on a port.  E.g., port 80 -> Apache(web server) , port 22 -> SSH server.

-If a port is open : something is running there, it could be vulnerable.

- **Port scanning** : checking which ports are open.
	- While scanning we can see: 
		- **Open** : a service is running, u can connect.
		- **Closed** : no service, but the system is reachable.
		- **Filtered** : blocked by firewall, u can't know what is inside. There could be services running or not, but the system is intentionally hiding something.

### Unfiltered

- Port is reachable
- No firewall blocking
- But state (open/closed) unknown

---

### open|filtered

- No response
- Could be open OR blocked

---

### closed|filtered

- Also unclear
- Could be closed OR blocked
### How scanning works

- Nmap sends request(packet) to a port. Then if it:
	- replies -> open
	- rejects -> closed
	- no response -> filtered


**Example**: If port 22 is open:      - SSH service running 
						- remote login possible
						- potential attack point  ( someone can try to login remotely)
		: If all ports filtered:  - firewall is blocking you
						- the system is hiding its services
						- could have vulnerabilities


# 3. Which OSI layer does Nmap interact

1. Transport layer:

What Nmap does at this layer:

- Sends TCP/UDP packets
- Checks:
    - Open ports
    - Closed ports
    - Filtered ports

- `nmap <target>`  : Nmap is Sending TCP packets to different ports and analyzing responses

 2. Network Layer (Layer 3)
 Used for **routing and addressing**

Nmap uses it to:

- Send packets to an **IP address**
- Perform host discovery (is the machine alive?)

 Example

- ICMP ping (like `ping`)
- IP-based scanning

3. Application Layer (Layer 7) — SOMETIMES
 Used when you enable advanced features

Example:

nmap -sV

Nmap:

- Talks to services (like HTTP, FTP)
- Tries to identify versions

| OSI Layer          | Role in Nmap                 |
| ------------------ | ---------------------------- |
| Layer 7 (App)      | Service/version detection    |
| Layer 5(Transport) | Port scanning (MAIN)         |
| Layer 3 (Network)  | IP targeting, host discovery |

Nmap primarily operates at the Transport Layer (Layer 4) because it scans TCP and UDP ports. It also uses the Network Layer (Layer 3) for IP addressing and host discovery, and the Application Layer (Layer 7) for service and version detection.


# How does TCP scan works

A **TCP scan** is when Nmap:
 Sends TCP packets to ports and analyzes how the target responds

### How TCP SYN scan works (-sS)
#### Step 1: Nmap sends SYN packet

To a port (example: port 80)

Nmap → SYN → Target
Meaning:
 “Hey, can I start a connection?”

#### Step 2: Target responds (3 possible ways)

#### Case 1: Port is OPEN

Target replies:

SYN-ACK
 Meaning:
 “Yes, I am listening on this port”

###  What Nmap does next:

Instead of completing connection:

Nmap → RST → Target

 Connection is **immediately closed**
####  Why?

To stay **stealthy**:
- No full connection
- Less logging
- Faster scanning

## Case 2: Port is CLOSED

Target replies:
RST
 Meaning:
 “No service here”
Nmap conclusion:
Port = CLOSED

Summary
1. Nmap → SYN →
2. Target response:
   SYN-ACK → OPEN
   RST     → CLOSED
   No reply→ FILTERED

- TCP scan = sending TCP packets
- SYN scan = most common
- Uses handshake behavior
- Does NOT complete connection
- Determines:
    - Open
    - Closed
    - Filtered


# How does UDP scan work

A **UDP scan** in **Nmap**:

 Sends UDP packets to ports and analyzes the responses.
It might send:
- Empty packet
- Protocol-specific packet (DNS, SNMP, etc.)

- `nmap -sU <target>`

 Summary

- UDP scan uses **UDP packets**
- No handshake
- Closed → ICMP unreachable
- Open/Filtered → often no response
- Harder to interpret.

### Why UDP scan is slower?

- since there is no handshake : Nmap waits for responses that never come in case of open | filtered.

- No handshake
- No responses
- Timeouts required: wait for a timeout bf deciding 
- Multiple retries


# OS detection

To identify:
- operating system type
- OS version
- Kernel version
- device 

-- `nmap -O <target>`

# NSE (Nmap scripting Engine)

It is a feature of **Nmap** that allows you to: run scripts to automate scanning, detection, and even basic exploitation

- Nmap with NSE can **interact with services and gather deeper information**.


# Common Nmap flags

- basic scan : `nmap <target>`  : scan top 1000TCP ports , default scan(SYN scan)
- specific ports : ` nmap -p 22,80 <target>`
	- `nmap -p- <target>` : scan all ports  65530 ports
- SYN Scan(-sS) : `nmap -sS <target>`  ,
- TCP connect scan(-sT) : `nmap -sT <target>`  , full tcp connection, used when not root . scan top 1000
- UDP scan: `nmap -sU <target>`
- Service version detection (-sV) : detect sw version
- OS detection (-o)
- Aggressive scan (-A) : Includes: OS detection, Version detection, Script scanning, Traceroute. is noisy (mareg miclewn hulu yaregal)  may be used in CTF but in real avoid it.
- Default script (-sC) : run safe NSE script
- --script : to run script
- pass port scan live : 
- -t0 &-t5 : t0 slow  t5 fast (yyazal betedegagami slemiteyk, open yehonen port liresa ychlal open yehonewn closed new lil ychlal )
- -PN kft new blo yamnal scan mareg yketlal

### Firewall Evasion

**Firewall evasion** is the technique of bypassing or avoiding detection by a firewall so that scanning or communication can still reach a target system.

A **firewall** is a security system that filters incoming and outgoing network traffic based on rules (like blocking certain ports, IPs, or protocols). Tools like Nmap are often detected and blocked by firewalls.

#### How Nmap Does Firewall Evasion

### 1. **Fragment Packets (`-f`)**

Break packets into smaller pieces.
Because some firewalls can’t properly reassemble fragmented packets → scan passes through

`nmap -f <target>`

### 2. **Change Source Port (`--source-port`)**

Use a trusted port like 80 or 53.
Because Firewalls often allow DNS (53) or HTTP (80), so scan may pass.

`nmap --source-port 53 <target>`

### 3. **Use Idle/Zombie Scan (`-sI`)**

Scan indirectly using another host.
- Target sees the zombie, not you
- Very stealthy but complex

`nmap -sI <zombie_host> <target>`

### 4. **Use TCP ACK Scan (`-sA`)**

Check firewall rules instead of open ports.
 Helps identify:
- Filtered vs unfiltered ports
- Firewall behavior

`nmap -sA <target>`

### 5. **Slow Down Scan (`-T`)**

Avoid detection by IDS/IPS.
 Timing levels:
- `-T0` → very slow (stealthy)
- `-T5` → very fast (easily detected)

`nmap -T0 <target>`

### 6. **Spoof Source IP (`-S`)**

Pretend to be another IP.
Requires advanced setup (raw packets + routing).
 
`nmap -S <fake_ip> <target>`


### What is an Nmap Xmas Scan?

An **Xmas scan** in Nmap is a stealthy scanning technique that sends specially crafted TCP packets with multiple flags turned on at once.

It’s called **“Xmas”** because the packet looks “lit up” like a Christmas tree.

#### How It Works

Normally, TCP packets use flags like:

- SYN → start connection
- ACK → acknowledge
- FIN → finish connection

But an Xmas scan sets **multiple unusual flags together**:

 **FIN + PSH + URG**
 
 This combination is **not normal behavior**, so different systems respond differently.

## Behavior of Ports

When you run:  `nmap -sX <target>`

**Open Port**
- **No response**
- Why? Open ports ignore weird packets

**Closed Port**
- Sends back **RST (reset)** packet

 **Filtered Port (firewall)**
- No response OR ICMP unreachable

### Why Is Xmas Scan Useful?

### 1. **Stealth**

- Doesn’t use normal SYN packets
- Can bypass simple firewalls

### 2. **Firewall Evasion**

- Some firewalls only block SYN scans
- Xmas scan may slip through

### 3. **OS Detection Clue**

- Some systems respond differently → helps fingerprint OS

**In an **Xmas scan** in Nmap, **these are the TCP flags that are turned on:**

 1. **FIN (Finish)**
 Means: **“I want to end/close the connection.”**
Normally used when a device is done communicating.

2. **PSH (Push)**
 Means: **“Deliver this data to the application immediately.”**
Normally tells the receiver not to wait/buffer—pass the data up right away.

3. **URG (Urgent)**
 Means: **“This packet contains urgent data.”**
Normally indicates some data should be treated as urgent.

##  Why it’s strange in an Xmas scan

These flags together: FIN + PSH + URG

are an unusual combination for a normal conversation.

It’s like sending a message that says:

- “Close the connection” (FIN)
- “Deliver data right now” (PSH)
- “And it’s urgent!” (URG)

 That weird mix is what makes it useful for probing how a target reacts.
