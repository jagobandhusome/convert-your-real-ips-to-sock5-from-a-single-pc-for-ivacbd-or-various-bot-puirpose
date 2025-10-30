# SOCKS5 Proxy Server

A lightweight, multi-threaded SOCKS5 proxy server implementation in Python that supports multiple binding addresses and ports.

## Features

- **SOCKS5 Protocol Support**: Full implementation of SOCKS5 protocol handshake and connection handling
- **Multi-Threaded**: Handles multiple client connections simultaneously
- **Multiple Bindings**: Can bind to multiple IP addresses and ports simultaneously
- **IPv4 and Domain Support**: Supports both IPv4 addresses and domain name connections
- **Traffic Relay**: Efficiently relays traffic between client and target servers
- **Cross-Platform**: Works on any platform that supports Python

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library modules)

## Installation

1. Clone or download the Python script `Create-Socks5.py`
2. Ensure Python is installed on your system

## Usage

### Basic Usage

Run the script with one or more binding addresses:

```bash
python Create-Socks5.py --bind_ip_port 0.0.0.0:1080 --bind_ip_port 127.0.0.1:1081
```
## Command Line Arguments
```
--bind_ip_port: Specify IP address and port to bind to (can be used multiple times)
```
## Examples
Single binding:

```bash
python Create-Socks5.py --bind_ip_port 0.0.0.0:1080
```
### Multiple bindings:

```bash
python Create-Socks5.py --bind_ip_port 0.0.0.0:1080 --bind_ip_port 127.0.0.1:1081 --bind_ip_port 192.168.1.100:1082
```
Localhost only:

```bash
python Create-Socks5.py --bind_ip_port 127.0.0.1:1080
```
### How It Works
Handshake: Performs SOCKS5 protocol handshake with client

Request Handling: Processes client connection requests

Connection Establishment: Connects to target server on behalf of client

Traffic Relay: Relays data bidirectionally between client and target server

Supported Address Types
IPv4 (ATYP = 1)

Domain Name (ATYP = 3)

IPv6 (ATYP = 4)

### Code Structure
Socks5Server class: Main thread class handling individual client connections

handle_handshake(): Performs SOCKS5 protocol negotiation

handle_client_request(): Processes client connection requests

relay_traffic(): Relays data between client and remote server

start_socks5_proxy(): Starts the proxy server listener

## Security Notes
⚠️ Important Security Considerations:

This proxy does not include authentication - anyone with network access can use it

Binding to 0.0.0.0 makes the proxy accessible from any network interface

Use firewall rules to restrict access as needed

Consider implementing authentication for production use

## Limitations
No authentication support

No UDP support (TCP only)

No logging or monitoring features

Basic error handling

### Contributing
Feel free to fork and submit pull requests for improvements such as:

Authentication support

UDP protocol support

Enhanced logging

Performance optimizations

Security enhancements

### License
This project is provided as-is for educational and development purposes.
