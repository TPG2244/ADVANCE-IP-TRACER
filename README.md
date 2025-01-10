# Advance IP Tracer

## Description
Advance IP Tracer is a Python-based tool designed to fetch detailed information about an IP address, supporting both IPv4 and IPv6. The tool uses the `ipapi` API to provide details such as location, ISP, timezone, and more. It is intended for educational purposes only.

---

## Features
- Fetches IP details such as city, region, country, and postal code.
- Displays latitude, longitude, and timezone of the IP address.
- Provides ISP, ASN, and organization information.
- Supports both IPv4 and IPv6.
- Handles interactive and non-interactive environments with a fallback IP option.

---

## Author
**Ronak (Arpan)**

---

## Prerequisites
Ensure the following are installed on your system:
- Python 3.6 or higher
- `requests` library

You can install the required library using:
```bash
pip install requests
```

---

## Usage
1. Clone or download the repository.
2. Run the tool using:
   ```bash
   python ip_tracker_tool.py
   ```
3. Enter the IP address (IPv4 or IPv6) when prompted. If input is not supported, the tool will default to `8.8.8.8`.

---

## Example Output
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
Postal Code: 94035
Latitude: 37.386
Longitude: -122.0838
Timezone: America/Los_Angeles
ASN: 15169
Organization: Google LLC
ISP: Google LLC
===============================

Tool execution completed.
AUTHOR: RONAK (ARPAN)
```

---

## API
This tool uses the `ipapi.co` API. For more information, visit the [IPAPI documentation](https://ipapi.co/).

---

## License
This project is for **educational purposes only** and should not be used for malicious activities.

---

## Contribution
Feel free to fork the repository and create pull requests for improvements or additional features.

---

## Disclaimer
The author is not responsible for any misuse of this tool. Always ensure compliance with local laws and regulations when using this software.

### Installation

- Just, Clone this repository -
  ```
  git clone --depth=1 https://github.com/TPG2244/ADVANCE-IP-TRACER
  ```

- Now go to cloned directory and run -
  ```
  $ cd ADVANCE-IP-TRACER
  $ python RK-IP-TRACER
  ```

**Conclusion**
Advanced IP Tracer is an essential tool for network administrators looking to improve their network management, security, and troubleshooting capabilities. With its powerful features like IP scanning, device detection, and performance monitoring, it offers significant benefits in maintaining a healthy and secure network environment. Whether you're managing a small home network or a large corporate system, Advanced IP Tracer is a valuable resource for ensuring efficient and effective network operations.
