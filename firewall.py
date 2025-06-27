import random
from ipaddress import ip_address


# firewall Class
class Firewall:
    # constructor
    def __init__(self, rules, log_file="firewall_log.txt"):
        self.rules = rules
        self.blocked_count = 0
        self.allowed_count = 0
        self.log_file = log_file

    # generate random ip
    def generate_random_ip(self):
        return f"192.168.1.{random.randint(0, 20)}"

    # check created random ip
    def check_ip(self, ip):
        action = self.rules.get(ip, "allow")
        if action == "block":
            self.blocked_count += 1
        else:
            self.allowed_count += 1

        return action

    # log of blocked and allowed ip
    def log_packet(self, ip_address, action, packet_id):
        with open(self.log_file, "a") as file:
            file.write(f"IP: {ip_address}, Action: {action.upper()}, Packet ID: {packet_id}\n")

    # traffic simulation
    def simulate_traffic(self, num_packets=12):
        for _ in range(num_packets):
            ip_address = self.generate_random_ip()
            action = self.check_ip()
            packet_id = random.randint(0, 9999)
            print(f"IP: {ip_address}, Action: {action.upper()}, Packet ID: {packet_id}")
            self.log_packet(ip_address, action, packet_id)

            print(f"\n Summary:")
            print(f"Blocked: {self.blocked_count}")
            print(f"AllowedL {self.allowed_count}")
