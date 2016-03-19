import xbox
import os
import urllib
import argparse


def save_clips(save_folder, clips):
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
        print("Created folder.")
    else:
        print("Folder already exists, continuing...")
    clip_count = 0  # I can't python
    for clip in clips:
        clip_json = clip.raw_json
        download_url = clip_json["gameClipUris"][0]["uri"]
        # video_name = clip_json["titleName"] + clip_json["dateRecorded"]
        video_name = "video" + clip_count.__str__()  # Like I said, I can't python
        file_name = os.path.join(save_folder, video_name + ".mp4")
        if not os.path.isfile(file_name):
            urllib.request.urlretrieve(download_url, file_name)
        else:
            print("Error, file \"" + file_name + "\" already exists!")
        clip_count += 1



def save_screenshots(save_folder, screenies):
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
        print("Created folder.")
    else:
        print("Folder already exists, continuing...")
    screenie_count = 0



def user_prompts():
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

    clips = gt.clips()
    clips = list(clips)
    save_clips(save_folder, clips)

def unattend():


def main():
    prompt = True
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-prompt", action='store_false', dest=prompt, help="Run the program without user prompts")

    if(prompt):
        user_prompts()
    else:
        unattend()


if __name__ == "__main__":
    main()

# TODO: commandline arguments
