import requests
import json
import time
import argparse

# Replace these with your actual API keys
client_id = "your_client_id"
client_secret = "your_client_secret"
username = "your_username"
password = "your_password"

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Spoof PSN level, trophy, or game completion percentage data.')
parser.add_argument('--action', choices=['level', 'trophy', 'percentage'], required=True, help='Action to perform: level, trophy, or percentage')
parser.add_argument('--type', choices=['temp', 'perm'], required=True, help='Type of spoof: temp (temporary) or perm (permanent)')
args = parser.parse_args()

# Authenticate with the PSN API
auth_url = "https://account.playstation.com/api/v1/oauth2/token"
auth_data = {
    "grant_type": "password",
    "client_id": client_id,
    "client_secret": client_secret,
    "username": username,
    "password": password,
    "redirect_uri": "http://localhost"
}
auth_response = requests.post(auth_url, data=auth_data)
access_token = json.loads(auth_response.text)["access_token"]

# Set the headers for the API requests
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Spoof the level, trophy, and game completion percentage data
level_data = {
    "level": {
        "levelId": "your_level_id",
        "levelName": "your_level_name",
        "levelDescription": "your_level_description",
        "levelIcon": "your_level_icon_url"
    }
}
trophy_data = {
    "trophy": {
        "trophyId": "your_trophy_id",
        "trophyName": "your_trophy_name",
        "trophyDescription": "your_trophy_description",
        "trophyIcon": "your_trophy_icon_url"
    }
}
percentage_data = {
    "percentage": {
        "gameId": "your_game_id",
        "completionPercentage": 100  # Set the desired completion percentage
    }
}

# Set the URLs for the API requests
level_url = "https://account.playstation.com/api/v1/users/" + username + "/"
trophy_url = "https://account.playstation.com/api/v1/users/" + username + "/trophies"
percentage_url = "https://account.playstation.com/api/v1/users/" + username + "/games/" + percentage_data["percentage"]["gameId"] + "/completion"

# Perform the specified action
if args.action == 'level':
    level_response = requests.put(level_url, headers=headers, json=level_data)
    if level_response.status_code == 200:
        print("Level spoofed successfully!")
        if args.type == 'temp':
            time.sleep(86400)  # Spoof for 1 day (86400 seconds)
            requests.delete(level_url, headers=headers)
            print("Temporary spoof ended.")
    else:
        print("Failed to spoof level!")
elif args.action == 'trophy':
    trophy_response = requests.put(trophy_url, headers=headers, json=trophy_data)
    if trophy_response.status_code == 200:
        print("Trophy spoofed successfully!")
        if args.type == 'temp':
            time.sleep(86400)  # Spoof for 1 day (86400 seconds)
            requests.delete(trophy_url, headers=headers)
            print("Temporary spoof ended.")
    else:
        print("Failed to spoof trophy!")
elif args.action == 'percentage':
    percentage_response = requests.put(percentage_url, headers=headers, json=percentage_data)
    if percentage_response.status_code == 200:
        print("Game completion percentage spoofed successfully!")
        if args.type == 'temp':
            time.sleep(86400)  # Spoof for 1 day (86400 seconds)
            requests.delete(percentage_url, headers=headers)
            print("Temporary spoof ended.")
    else:
        print("Failed to spoof game completion percentage!")