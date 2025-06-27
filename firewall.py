import random

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

    # traffic simulation