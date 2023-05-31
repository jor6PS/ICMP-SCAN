import argparse
import ipaddress
import subprocess
import concurrent.futures
import re

def ping_ip(ip):
    try:
        output = subprocess.check_output(['ping', '-c', '1', '-W', '1', str(ip)], stderr=subprocess.STDOUT, universal_newlines=True)
        if re.search(r"1 packets transmitted, 1 received, 0% packet loss", output):
            result = str(ip) + " is up"
        else:
            result = str(ip) + " is down"
    except subprocess.CalledProcessError:
        result = str(ip) + " is down"
    
    with open('results.txt', 'a') as f:
        f.write(result + '\n')
    
    print(result)

def scan_network(network, num_threads):
    ip_list = list(ipaddress.ip_network(network).hosts())
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = executor.map(ping_ip, ip_list)

def main():
    parser = argparse.ArgumentParser(description='ICMP Scanner')
    parser.add_argument('-r', '--range', type=str, help='IP range to scan in CIDR notation', required=True)
    parser.add_argument('-t', '--threads', type=int, help='Number of threads to use (default: 10)', default=10)
    args = parser.parse_args()

    network = args.range
    num_threads = args.threads

    scan_network(network, num_threads)

if __name__ == '__main__':
    main()
