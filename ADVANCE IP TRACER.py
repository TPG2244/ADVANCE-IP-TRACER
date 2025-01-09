import requests
import json

def main():
    print("===============================")
    print("        ADVANCE IP-TRACER       ")
    print("       AUTHOR: RONAK (ARPAN)    ")
    print("===============================")
    print("      ONLY FOR EDUCATIONAL PURPOSE")
    print("===============================\n")

    # Attempt to get user input or use a fallback in restricted environments
    ip_address = "8.8.8.8"  # Default fallback IP address
    try:
        ip_address = input("Enter the IP address (IPv4 or IPv6): ").strip()
        if not ip_address:
            print("No IP address provided. Using default IP address.")
    except OSError:
        print("Input operation is not supported in this environment. Using default IP address.")

    print(f"Using IP address: {ip_address}\n")
    print("Fetching details, please wait...\n")

    # API call for IP data
    try:
        response = requests.get(f"https://ipapi.co/{ip_address}/json/")
        if response.status_code == 200:
            ip_data = response.json()

            # Check if the response contains an error
            if 'error' in ip_data:
                print("Error fetching IP details: ", ip_data.get('reason', 'Unknown error'))
            else:
                print("===============================")
                print("         IP DETAILS             ")
                print("===============================")
                print(f"IP Address: {ip_data.get('ip', 'N/A')}")
                print(f"City: {ip_data.get('city', 'N/A')}")
                print(f"Region: {ip_data.get('region', 'N/A')}")
                print(f"Country: {ip_data.get('country_name', 'N/A')} ({ip_data.get('country_code', 'N/A')})")
                print(f"Postal Code: {ip_data.get('postal', 'N/A')}")
                print(f"Latitude: {ip_data.get('latitude', 'N/A')}")
                print(f"Longitude: {ip_data.get('longitude', 'N/A')}")
                print(f"Timezone: {ip_data.get('timezone', 'N/A')}")
                print(f"ASN: {ip_data.get('asn', 'N/A')}")
                print(f"Organization: {ip_data.get('org', 'N/A')}")
                print(f"ISP: {ip_data.get('isp', 'N/A')}")
                print("===============================\n")
        else:
            print(f"Failed to fetch IP details. HTTP Error Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the IP details:", str(e))

    print("\nTool execution completed.")
    print("AUTHOR: RONAK (ARPAN)")

if __name__ == "__main__":
    main()
