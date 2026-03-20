# NETWORK SECURITY REPORT

## Team Name: Group 1 Network Security Analysts
## Date: July 16, 2025
 
## Task Objective
- To identify and investigate suspicious activities in the organization’s network and to recommend actions to secure the network in alignment with the Network
  Security Policy.

## Analysis
- Identify Anomalies
  - Are there any strange IPs?
    - 94.102.49.12: This external IP is not part of the device mappings in the internal network
    - 10.0.0.1: This IP is within the internal range but is undocumented in internal_devices.txt, indicating a potential misconfiguration or rogue device. For this reason, we do not believe fully that the IP is a strange one

  - Are any services exposed that shouldn’t be?
    - FTP and Telnet: These unencrypted services are insecure, exposing credentials and data to interception
    - HTTP: Unencrypted HTTP is vulnerable to man-in-the-middle attacks
    - RPC: By research, we found out that, RPC is a high-risk service found to be vulnerable to exploitation

  - Do you notice repeated connection attempts or unusual ports?
    - We noticed the log at [2025-04-22 08:14:22] showing 10.0.0.15 sending repeated requests to 10.0.0.25 on port 135 which was a usual port stated in the internal device mapping
    - Port 6667 was unusual in the connection from 192.168.1.100 to 94.102.49.12

- Spot Vulnerabilities
  - Machines Running Insecure Services
  - 10.0.0.15 (Workstation HR) running FTP and Telnet
  - 192.168.1.100 (IoT Camera): running FTP and Telnet
  - 10.0.0.17 (Web Server) and 192.168.1.101 (Web Interface) running HTTP
  - 10.0.0.25 (Domain Controller) running RPC which might be insecure

- Any devices communicating externally on unusual ports?
  - IoT camera communicated externally on port 6667

## Recommended Fixes
- Which ports should be blocked or restricted?
  - Block Ports 21 (FTP) and 23 (Telnet)
  - Block Port 6667 (IRC)
  - Restrict Port 135 (RPC): Use firewall rules to limit RPC access to trusted internal systems
  - Restrict Port 80 (HTTP): Configure firewall rules to redirect HTTP traffic to HTTPS

- Which services should be disabled or updated?
  - Disable FTP and Telnet and replace with SFTP and SSH
  - Upgrade HTTP to HTTPS
  - Harden RPC: Ensure the RPC service is patched against vulnerabilities

- Should firewall rules be changed? Yes…
  - Implement firewall rules to block FTP (port 21), Telnet (port 23), and IRC (port 6667) across all devices
  - Use firewall rules to isolate IoT devices from critical systems allowing only necessary traffic
  - Configure firewall rules to place critical systems in a DMZ, restricting external access
  - Implement firewall rules to log and restrict traffic to/from 10.0.0.1 until its role is verified
  - Firewall rules must work with NIDS/NIPS to block detected threats
