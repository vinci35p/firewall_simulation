import random
# firewall Class
class Firewall:
    # constructor
    def __init__(self, ip_rules, port_rules=None, log_file="firewall_log"):
        self.ip_rules = ip_rules
        self.port_rules = port_rules if port_rules else []
        self.blocked_count = 0
        self.allowed_count = 0
        self.log_file = log_file
        self.blocked_by_port = {}

        with open(self.log_file, "w") as file:
            file.write("=== FIREWALL LOG START ===\n")

    # generate random ip
    def generate_random_ip(self):
        return f"192.168.1.{random.randint(0, 20)}"

    # generate random port
    def generate_random_port(self):
        return random.choice([22, 80, 443, 8080, 3306])

    # check created random ip
    def check_ip(self, ip_address, port):
        action = "allow"

        if self.ip_rules.get(ip_address) == "block":
            action = "block"

        if port in self.port_rules:
            action = "block"
            self.blocked_by_port[port] = self.blocked_by_port.get(port, 0) + 1

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
            action = self.check_ip(ip_address)
            packet_id = random.randint(0, 9999)
            print(f"IP: {ip_address}, Action: {action.upper()}, Packet ID: {packet_id}")
            self.log_packet(ip_address, action, packet_id)

        print(f"\nSummary:")
        print(f"Blocked: {self.blocked_count}")
        print(f"Allowed: {self.allowed_count}")
