# Python Networking Tools

## Description
This repository is here to store all my coded networking tools.

# Network Scanner with Nmap

## Description
This Python script utilizes Nmap for network scanning, enabling users to scan for open ports on a specified IP address within a given port range. It provides an interactive interface to perform scans and optionally save the results to a file.

## Requirements
- Python 3.x
- Nmap
- Please ensure you have nmap installed on your system and added to the PATH environmental variable before use

## Usage
1. Clone this repository.
2. Install Nmap if not already installed (`sudo apt-get install nmap` on Debian-based systems).
3. Run the script:
    ```
    python network_scanner.py [IP_ADDRESS PORT_RANGE]
    ```
    If no arguments are provided, the script will prompt for the IP address and port range interactively.

## Sample Output
After running the script, the output might resemble:
Host : 192.168.1.1 (router.example.com)
State : up

---------
Protocol : tcp
port : 22    state : open
port : 80    state : open
