# Network Connectivity Checker
import socket
import subprocess
import platform
import sys

def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
    """
    Check if device has internet connectivity by pinging a known host
    """
    try:
        socket.create_connection((host, port), timeout=timeout)
        return True
    except (socket.timeout, socket.error):
        return False

def ping_host(host):
    """
    Ping a specific host to check connectivity
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    
    try:
        result = subprocess.run(command, capture_output=True, timeout=5)
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False

if __name__ == "__main__":
    print("Checking internet connectivity...")
    
    if check_internet_connection():
        print("✓ Internet connection is active")
    else:
        print("✗ No internet connection")
    
    # Test specific hosts
    hosts = ["google.com", "github.com", "cloudflare.com"]
    print("\nPinging specific hosts:")
    for host in hosts:
        status = "✓" if ping_host(host) else "✗"
        print(f"{status} {host}")
