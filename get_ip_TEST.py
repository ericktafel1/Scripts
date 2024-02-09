import importlib.util
import requests
import sys

# Function to upload message to Pastebin
def upload_to_pastebin(ip_address):
    pastebin_api_url = 'https://pastebin.com/api/api_post.php'
    pastebin_dev_key = 'your_pastebin_dev_key'
    
    try:
        # Compose message
        message = f'Public IP address: {ip_address}'
        
        # Send message to Pastebin
        data = {
            'api_dev_key': pastebin_dev_key,
            'api_option': 'paste',
            'api_paste_code': message,
            'api_paste_private': '1',  # 1 - Unlisted, 0 - Public
            'api_paste_expire_date': '1D'  # Expiration date (1 day)
        }
        response = requests.post(pastebin_api_url, data=data)
        
        # Check if the request was successful
        if response.status_code == 200 and response.text.startswith('https://pastebin.com/'):
            print("IP address uploaded to Pastebin successfully!")
            print("Pastebin URL:", response.text.strip())
        else:
            print("Failed to upload IP address to Pastebin.")
            print("Response:", response.text)
    except Exception as e:
        print("Failed to upload IP address to Pastebin:", e)

# Placeholder function to simulate getting public IP address
def get_public_ip():
    return '192.0.2.1'  # Placeholder IP address for testing

if __name__ == "__main__":
    public_ip = get_public_ip()
    print("Your public IP address is:", public_ip)
    
    # Upload IP address to Pastebin
    upload_to_pastebin(public_ip)
