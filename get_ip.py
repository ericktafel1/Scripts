import importlib.util
import sys

# Check if the requests module is installed
try:
    import requests
except ImportError:
    print("The 'requests' module is not installed. Attempting to install it...")
    
    # Try to install requests module using pip
    try:
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
        
        # Import the requests module after installation
        import requests
    except Exception as e:
        print("Failed to install the 'requests' module:", e)
        sys.exit(1)

def get_public_ip():
    try:
        # Make a GET request to a public IP lookup service
        response = requests.get('https://api.ipify.org?format=json')
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the IP address from the JSON response
            ip_address = response.json()['ip']
            return ip_address
        else:
            return "Failed to retrieve IP address"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    public_ip = get_public_ip()
    print("Your public IP address is:", public_ip)
    input("Press Enter to exit...")
