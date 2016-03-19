import xbox
import os
import urllib


user = input("Enter username: ")
pwd = input("Enter password: ")
gtag = input("Enter gamertag: ")

try:
    print("Attempting to authenticate...")
    xbox.client.authenticate(login=user, password=pwd)
except:
    print("Authentication failed!")
else:
    print("Authentication successful!")


gt = xbox.GamerProfile.from_gamertag(gtag)

save_folder = input("Enter name of folder you want to save user's clips to: ")
if not os.path.exists(save_folder):
    os.mkdir(save_folder)
else:
    print("Folder exists, continuing...")

clips = gt.clips()
clips = list(clips)
count = 0  # I can't python
for clip in clips:
    clip_json = clip.raw_json
    download_url = clip_json["gameClipUris"][0]["uri"]
    # video_name = clip_json["titleName"] + clip_json["dateRecorded"]
    video_name = "video" + count.__str__()  # Like I said, I can't python
    file_name = os.path.join(save_folder, video_name + ".mp4")
    if not os.path.isfile(file_name):
        urllib.request.urlretrieve(download_url, file_name)
    else:
        print("Error, file \"" + file_name + "\" already exists!")
    count += 1

# TODO: commandline arguments
