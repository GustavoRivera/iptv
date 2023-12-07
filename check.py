import requests

def check_urls(file_path):
    valid_channels = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_channel = None

    for line in lines:
        if line.startswith("#EXTINF:"):
            current_channel = line.strip()
        elif line.startswith("http://") or line.startswith("https://"):
            url = line.strip()
            try:
                response = requests.head(url, timeout=5)
                if response.status_code == 200:
                    valid_channels.append(current_channel)
                    valid_channels.append(url)
            except requests.RequestException:
                pass  # URL is not valid, skip it

    return valid_channels

# Use the function with your M3U file
file_path = 'sorted_channels.m3u'
working_channels = check_urls(file_path)

# Optionally, write the working channels back to a new M3U file
with open('final_channels.m3u', 'w') as file:
    file.write("#EXTM3U\n")
    file.writelines("\n".join(working_channels))
