# from firewall import the class
from firewall import Firewall

if __name__ == "__main__":
    firewall_ip_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block"
    }

    firewall_port_rules = [22, 3306]

    # run the code
    fire_w = Firewall(ip_rules=firewall_ip_rules, port_rules=firewall_port_rules)
    fire_w.simulate_traffic(num_packets=15)