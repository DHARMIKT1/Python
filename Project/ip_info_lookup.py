import requests
import pycountry

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        country_code = data.get('country')
        region = data.get('region')
        city = data.get('city')
        isp = data.get('org')
        loc = data.get('loc')  # Location in "latitude,longitude" format
        
        if country_code:
            country = pycountry.countries.get(alpha_2=country_code)
            country_name = country.name if country else "Unknown country"
        else:
            country_name = "Country not found"
        
        return country_name, region, city, isp, loc
    except Exception as e:
        return f"Error: {e}", None, None, None, None

# Get user input for IP address
ip_address = input("Enter the IP address: ")

# Get IP information
country, region, city, isp, loc = get_ip_info(ip_address)

# Display the results
print(f"The IP address {ip_address} belongs to:")
print(f"Country: {country}")
print(f"State/Region: {region}")
print(f"City: {city}")
print(f"ISP Provider: {isp}")
print(f"Location (Latitude, Longitude): {loc}")


'''
Steps to Run the Script:

1. Install Required Libraries: Open your terminal or command prompt and install the required libraries using pip:
        - pip install requests pycountry
2. Download the Script: Save the script as ip_info_lookup.py in your desired directory.
3. Run the Script: Navigate to the directory where you saved the script and run it using Python:
        - python ip_info_lookup.py
4. Enter the IP Address: When prompted, enter the IP address you want to look up. The script will then display the country, state/region, city, ISP provider, and location (latitude and longitude) associated with the IP address.

'''
