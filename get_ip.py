import importlib.util
import requests
import sys

# Function to post message to Reddit
def post_to_reddit(ip_address):
    reddit_api_url = 'https://www.reddit.com/api/v1/access_token'
    subreddit = 'your_subreddit'
    
    try:
        # Compose message
        message = f'Public IP address: {ip_address}'
        
        # Authenticate with Reddit API (if required)
        # Replace 'client_id', 'client_secret', 'username', and 'password' with appropriate values
        auth = requests.auth.HTTPBasicAuth('client_id', 'client_secret')
        data = {'grant_type': 'password', 'username': 'username', 'password': 'password'}
        headers = {'User-Agent': 'your_user_agent'}
        response = requests.post(reddit_api_url, auth=auth, data=data, headers=headers)
        access_token = response.json()['access_token']
        
        # Post message to subreddit
        url = f'https://oauth.reddit.com/r/{subreddit}/submit'
        headers = {'Authorization': f'Bearer {access_token}', 'User-Agent': 'your_user_agent'}
        data = {'title': 'Public IP Address', 'text': message, 'kind': 'self'}
        response = requests.post(url, headers=headers, data=data)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("IP address posted to Reddit successfully!")
        else:
            print("Failed to post IP address to Reddit. Status code:", response.status_code)
    except Exception as e:
        print("Failed to post IP address to Reddit:", e)

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
    
    # Post IP address to Reddit
    post_to_reddit(public_ip)
