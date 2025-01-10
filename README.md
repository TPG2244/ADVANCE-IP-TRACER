# Advance IP Tracer

**Author**: Ronak (Arpan) 

**STUDENT**: Kendriya Vidyalay Sangathan 2 NSB 

**AGE**:16+

**Purpose**: Only for Educational Use  

Advance IP Tracer is a Python-based tool designed for tracing details about an IP address (IPv4 or IPv6). This tool provides information such as location, ISP, organization, timezone, and more. It is a simple yet powerful utility for networking and educational purposes.

---

## Features
- Supports both IPv4 and IPv6.
- Fetches geographical and organizational details of an IP address.
- Provides fallback to a default IP address (8.8.8.8) in non-interactive environments.
- Lightweight and easy to use.

---

## Requirements

To use this tool on Kali Linux, ensure the following prerequisites are met:

- Python 3.6 or higher
- Internet connection (required to fetch IP details via API)
- `requests` library for Python

You can install the `requests` library with the following command:
```bash
pip install requests
```

---

## Installation

1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/TPG2244/ADVANCE-IP-TRACER
   ```

2. Navigate to the tool directory:
   ```bash
   cd Advance-IP-Tracer
   ```


---

## Usage

1. Run the script:
   ```bash
   python3 RK-IP-TRACER
   ```

2. Enter the desired IP address (IPv4 or IPv6) when prompted. If no input is provided, the tool will default to tracing `8.8.8.8`.

Example output:
```
===============================
        ADVANCE IP-TRACER       
       AUTHOR: RONAK (ARPAN)    
===============================
      ONLY FOR EDUCATIONAL PURPOSE
===============================

Enter the IP address (IPv4 or IPv6): 8.8.8.8
Using IP address: 8.8.8.8
Fetching details, please wait...

===============================
         IP DETAILS             
===============================
IP Address: 8.8.8.8
City: Mountain View
Region: California
Country: United States (US)
Postal Code: 94043
Latitude: 37.4056
Longitude: -122.0775
Timezone: America/Los_Angeles
ASN: 15169
Organization: Google LLC
ISP: Google LLC
===============================

Tool execution completed.
AUTHOR: RONAK (ARPAN)
```

---

## Notes
- Ensure you have an active internet connection to use the API service.
- The tool uses the [ipapi.co](https://ipapi.co/) API for fetching IP details.
- If input operations are restricted in your environment, the tool will automatically use the fallback IP (`8.8.8.8`).

---

## Disclaimer
This tool is intended for **educational purposes only**. Unauthorized usage of this tool may violate applicable laws and regulations. The author assumes no responsibility for any misuse or damage caused.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Happy Tracing!


### Installation (METHOD 2ND)

- Just, Clone this repository -
  ```
  git clone https://github.com/TPG2244/ADVANCE-IP-TRACER
  ```

- Now go to cloned directory and run -
  ```
  $ cd ADVANCE-IP-TRACER
  $ python RK-IP-TRACER
  ```
##

<p align="left">
  <a href="https://shell.cloud.google.com/cloudshell/open?cloudshell_git_repo=https://github.com/htr-tech/zphisher.git&tutorial=README.md" target="_blank">
</p>

## 

**Conclusion**
Advanced IP Tracer is an essential tool for network administrators looking to improve their network management, security, and troubleshooting capabilities. With its powerful features like IP scanning, device detection, and performance monitoring, it offers significant benefits in maintaining a healthy and secure network environment. Whether you're managing a small home network or a large corporate system, Advanced IP Tracer is a valuable resource for ensuring efficient and effective network operations.
