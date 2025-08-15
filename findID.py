import configparser
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Load config from config.ini
config = configparser.ConfigParser()
config.read('config.ini')
API_KEY = config['settings']['api_key']

# Build the YouTube service
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Read handles from handle.txt
with open('handle.txt', 'r') as file:
    handles = [line.strip() for line in file if line.strip()]

# Prepare results list
results = []

for handle in handles:
    try:
        # Make API request to get channel ID using forHandle
        request = youtube.channels().list(
            part='id',
            forHandle=handle
        )
        response = request.execute()
        
        if 'items' in response and len(response['items']) > 0:
            channel_id = response['items'][0]['id']
        else:
            channel_id = 'Not found'
    except HttpError as e:
        channel_id = f'Error: {e.resp.status} - {e.reason}'
    except Exception as e:
        channel_id = f'Error: {str(e)}'
    
    results.append([handle, channel_id])

# Write to result.txt
with open('result.txt', 'w') as txtfile:
    for handle, channel_id in results:
        txtfile.write(f"- [{handle}]([{channel_id}])\n")

print("Processing complete. Results saved to result.txt")