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
with open('handle.txt', 'r', encoding='utf-8') as file:
    handles = [line.strip() for line in file if line.strip()]

# Prepare results list
results = []

for handle in handles:
    try:
        # Make API request to get channel ID and title using forHandle
        request = youtube.channels().list(
            part='id,snippet',
            forHandle=handle
        )
        response = request.execute()
        
        if 'items' in response and len(response['items']) > 0:
            channel_id = response['items'][0]['id']
            channel_name = response['items'][0]['snippet']['title']
        else:
            channel_id = 'Not found'
            channel_name = 'Not found'
    except HttpError as e:
        channel_id = f'Error: {e.resp.status} - {e.reason}'
        channel_name = 'Error'
    except Exception as e:
        channel_id = f'Error: {str(e)}'
        channel_name = 'Error'
    
    results.append([channel_name, handle, channel_id])

# Write to result.txt
with open('result.txt', 'w', encoding='utf-8') as txtfile:
    for channel_name, handle, channel_id in results:
        txtfile.write(f"- {channel_name} @{handle} ({channel_id})\n")

print("Processing complete. Results saved to result.txt")