import csv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Placeholder for your YouTube Data API v3 key
# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = ''

# Build the YouTube API service
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Read handles from handle.txt
with open('handle.txt', 'r') as file:
    handles = [line.strip() for line in file.readlines() if line.strip()]

# Prepare to write to result.csv
with open('result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['handle', 'creator ID'])

    for handle in handles:
        # Remove leading '@' if present, as API expects handle without it
        clean_handle = handle.lstrip('@')
        
        try:
            # Call the API to get channel ID using forHandle
            response = youtube.channels().list(
                part='id',
                forHandle=clean_handle
            ).execute()
            
            if 'items' in response and response['items']:
                channel_id = response['items'][0]['id']
                writer.writerow([handle, channel_id])
            else:
                writer.writerow([handle, 'Not Found'])
        except HttpError as e:
            writer.writerow([handle, f'Error: {e}'])
        except Exception as e:
            writer.writerow([handle, f'Unexpected Error: {str(e)}'])

print("Processing complete. Results saved to result.csv")