import subprocess

# wifi Password extractor and saver in .txt format
# first entering command to capture all the profiles in a dict
# secondly running a loop in command and replace profile name with dict words one by one, make sure key=clear
def show_wifi_profiles():
    result = subprocess.run(['netsh', 'wlan', 'show', 'profile'], capture_output=True, text=True)
    output = result.stdout
    profiles = {}
    for line in output.splitlines():
        if "All User Profile" in line:
            profile_name = line.split(":")[1].strip()
            profiles[profile_name] = profile_name
    return profiles


def show_profile_details(profiles, filename):
    with open(filename, 'w') as file:
        for profile_name in profiles.values():
            result = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear'], capture_output=True, text=True)
            output = result.stdout
            file.write("print(******* WIFI Full Detail Extractor by Mamuli *******)\n")
            file.write(output)
            file.write("\n")


wifi_profiles = show_wifi_profiles()
show_profile_details(wifi_profiles, 'wifi_details.txt')
print(f"Script Finished Data Saved to wifi_details.txt..")
