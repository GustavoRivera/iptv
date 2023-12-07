
import re
# Revised Python code to more accurately remove the leading numbers and hyphens from channel names

def sort_and_clean_m3u_file_v2(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    channels = []
    current_channel = None

    for line in lines:
        if line.startswith("#EXTINF:"):
            # Extract channel name and remove leading numbers and hyphens
            channel_name = line.split(',', 1)[-1].strip()
            cleaned_name = re.sub(r'^\d+\s*-\s*\d+\s*|\d+\s*-\s*|\d+\s*', '', channel_name)
            current_channel = cleaned_name
        elif line.startswith("http://") or line.startswith("https://"):
            if current_channel:
                channels.append((current_channel, line.strip()))
                current_channel = None

    # Sort channels by name
    sorted_channels = sorted(channels, key=lambda x: x[0])

    # Write the sorted channels to a new M3U file
    with open(output_file_path, 'w') as file:
        file.write("#EXTM3U\n")
        for name, url in sorted_channels:
            file.write(f"#EXTINF:-1,{name}\n{url}\n")

    return output_file_path

# Define the input and output file paths
input_m3u_file = "input_channels.m3u"  # Temporary file path for this example
output_m3u_file = "sorted_channels.m3u"

# # Simulating the process by writing the user's provided data to the input file
# input_data = """#EXTM3U
# #EXTINF:-1,21 - 252 ComedyC
# http://181.78.105.146:2000/play/a04a
# #EXTINF:-1,23 - 290 CartoonNetwork
# http://181.78.105.146:2000/play/a03k
# ... (other channels)"""

# with open(input_m3u_file, "w") as file:
#     file.write(input_data)

# Call the function to sort and create a new M3U file
cleaned_sorted_file_path_v2 = sort_and_clean_m3u_file_v2(input_m3u_file, output_m3u_file)
cleaned_sorted_file_path_v2

