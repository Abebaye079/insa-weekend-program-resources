import socket
from datetime import datetime
import threading

# --------------------
# Parse port input
# --------------------
def parse_ports(port_input):
    ports = set()
    parts = port_input.split(",")

    for part in parts:
        part = part.strip()

        if "-" in part:
            start, end = part.split("-")
            ports.update(range(int(start), int(end) + 1))
        else:
            ports.add(int(part))

    return sorted(ports)


# --------------------
# TCP scan function
# --------------------
def scan_tcp(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(2)

    try:
        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"\nPort {port} : OPEN")

            try:
                # HTTP ports → send proper request
                if port == 80:
                    s.send(f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n".encode())
                    banner = s.recv(1024).decode(errors='ignore').strip()
                    lines = banner.split("\r\n")[:5]
                    print("Banner:")
                    for line in lines:
                        print(line)

                # SSH (just receive)
                elif port == 22:
                    banner = s.recv(1024).decode(errors='ignore').strip()
                    print(f"Banner: {banner}")

                # Other ports
                else:
                    s.send(b"Hello\r\n")
                    banner = s.recv(1024).decode(errors='ignore').strip()
                    print(f"Banner: {banner}")

            except:
                print("Banner: Not received")

        else:
            print(f"Port {port} (TCP): CLOSED")

    except Exception as e:
        print(f"Port {port} (TCP): ERROR - {e}")

    finally:
        s.close()


# --------------------
# UDP scan function
# --------------------
def scan_udp(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.setdefaulttimeout(2)

    try:
        s.sendto(b"", (target_ip, port))
        data, _ = s.recvfrom(1024)
        print(f"Port {port} (UDP): OPEN (response received)")

    except socket.timeout:
        print(f"Port {port} (UDP): OPEN or FILTERED")

    except Exception as e:
        print(f"Port {port} (UDP): CLOSED ({e})")

    finally:
        s.close()


# --------------------
# Main program
# --------------------
target = input("Enter target (IP or domain): ")
port_input = input("Enter ports (e.g. 80 or 20-100 or 22,80,443): ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname")
    exit()

ports = parse_ports(port_input)

print(f"\nStarting TCP + UDP scan with Banner Grabbing on {target_ip}")
print("-" * 50)

start_time = datetime.now()

# --------------------
# Run TCP threads
# --------------------
print("\n[TCP SCAN + BANNER]")
tcp_threads = []

for port in ports:
    t = threading.Thread(target=scan_tcp, args=(port,))
    tcp_threads.append(t)
    t.start()

for t in tcp_threads:
    t.join()  # Wait for all threads to finish

# --------------------
# Run UDP threads
# --------------------
print("\n[UDP SCAN]")
udp_threads = []

for port in ports:
    t = threading.Thread(target=scan_udp, args=(port,))
    udp_threads.append(t)
    t.start()

for t in udp_threads:
    t.join()

end_time = datetime.now()
print("-" * 50)
print(f"Scan completed in: {end_time - start_time}")