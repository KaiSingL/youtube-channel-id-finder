YouTube Handle to Channel ID Converter
Description
This Python script utilizes the YouTube Data API v3 to retrieve channel IDs from given YouTube handles. It reads a list of handles from a text file, fetches the corresponding channel IDs using the API, and outputs the results in a formatted text file.
Features

Reads handles from handle.txt (one handle per line, e.g., @examplehandle).
Uses an API key stored in config.ini for authentication.
Handles errors gracefully, such as invalid handles or API issues.
Outputs results to result.txt in the format:- [handle]([channel ID])



Requirements

Python 3.x
google-api-python-client library (install via pip install google-api-python-client)
configparser (included in Python standard library)

Setup

Install the required library:
pip install google-api-python-client


Create a config.ini file in the same directory as the script with the following content:
[settings]
api_key = YOUR_YOUTUBE_API_KEY_HERE

Replace YOUR_YOUTUBE_API_KEY_HERE with your actual YouTube Data API v3 key. You can obtain an API key from the Google Developers Console.

Prepare handle.txt with the YouTube handles you want to process, one per line.


Usage
Run the script from the command line:
python script.py

The script will process each handle, fetch the channel ID, and save the results to result.txt. A completion message will be printed to the console.
Example
handle.txt:
MrBeast
PewDiePie

result.txt (example output):
- MrBeast (UCX6OQ3DkcsbYNE6H8uQQuVA)
- PewDiePie (UC-lHJZR3Gqxm24_Vd_AJ5Yw)

Error Handling

If a handle is not found, it will output Not found.
API errors will be captured and output in the format Error: status - reason.

Limitations

Subject to YouTube API quotas and rate limits.
Handles must start with @ as per YouTube's format.

License
This project is open-source and available under the MIT License.