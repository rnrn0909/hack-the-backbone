# Hacking the Backbone

**Hacking the Backbone: Shell Reverse Attacks on IIoT Systems**

Case study using Fischertechnik's Lernfabrik 4.0 (9V)

## This repository includes
- The script for the reverse shell server (`server.py`) and client (`client.py`)

## How to use it?

1. **Setting up the Client (Victim Device)**
   - `client.py` is the reverse shell payload that needs to be run on the victim device.
   - Before running this script, change the following variables:
     - `SERVER_HOST = "<Attacker_IP>"`
     - `SERVER_PORT = <Attacker Port>`

2. **Setting up the Server (Attacker's PC)**
   - `server.py` is the reverse shell listener that needs to be run on the attacker's PC.

## Required Packages
- `socket`

### Steps to Run

1. **On the Attacker's PC:**
   - Open a terminal and navigate to the directory containing `server.py`.
   - Run the server script:
     ```
     python server.py
     ```

2. **On the Victim Device:**
   - Transfer `client.py` to the victim device.
   - Open a terminal on the victim device and navigate to the directory containing `client.py`.
   - Run the client script:
     ```
     python client.py
     ```

Once both scripts are running, the reverse shell connection will be established, providing the attacker with remote access to the victim device.

---

#### ⚡[Video](https://youtu.be/u8nhV5LXjJU)

**Disclaimer:** This project is intended for educational purposes only. Unauthorized use of these scripts for malicious purposes is illegal and unethical. Always obtain proper authorization before testing security on any system.




<img src="https://github.com/rnrn0909/beyondthelens/assets/57967202/236eb741-b6dc-4f8a-89b1-ebfc66ee2a2e" align="right" width="260" height="40">
