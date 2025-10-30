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
