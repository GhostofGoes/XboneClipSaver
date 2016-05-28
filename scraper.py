#!/usr/bin/env python3
# scraper.py

import xbox
import os
import logging
import urllib
import argparse


class XboxScraper:

    def __init__(self, silent=False, clip_folder="clips", screenshot_folder="screenshots"):
        if silent:
            logging.basicConfig(filename='XboxScraper.log', level=logging.INFO)
        else:
            logging.basicConfig(level=logging.INFO)
        self.clip_folder = clip_folder
        self.make_folder(clip_folder)
        self.screenshot_folder = screenshot_folder
        self.make_folder(screenshot_folder)

    def save_clips(self, clips):
        """ Downloads all game clips to a given folder """
        clip_count = 0  # I can't python
        for clip in clips:
            clip_json = clip.raw_json
            download_url = clip_json["gameClipUris"][0]["uri"]
            # video_name = clip_json["titleName"] + clip_json["dateRecorded"]
            video_name = "video" + clip_count.__str__()  # Like I said, I can't python
            file_name = os.path.join(self.save_folder, video_name + ".mp4")
            if not os.path.isfile(file_name):
                urllib.request.urlretrieve(download_url, file_name)
            else:
                logging.error("Error, file %s already exists!", file_name)
            clip_count += 1

    # TODO: implement screenshot saving, possibly using code in old/scraper2.py
    def save_screenshots(self, screenshots):
        """ Downloads all screenshots to a given folder """
        screenie_count = 0

    def user_prompts(self):
        self.user = input("Enter username: ")
        self.pwd = input("Enter password: ")
        self.gtag = input("Enter gamertag: ")

        self.login()
        try:
            logging.info("Attempting to pull gamertag info for the gamertag %s", self.gtag)
            gt = xbox.GamerProfile.from_gamertag(self.gtag)
        except xbox.exceptions.GamertagNotFound:
            logging.error("Gamertag not found!")

        clips = list(gt.clips())
        screenshots = []
        self.save_clips(clips)
        self.save_screenshots(screenshots)

    def login(self):
        try:
            logging.info("Attempting to authenticate...")
            xbox.client.authenticate(login=self.user, password=self.pwd)
        except xbox.exceptions.AuthenticationException:
            logging.error("Authentication failed!")
        else:
            logging.info("Authentication successful!")

    @staticmethod
    def make_folder(save_folder):
        if not os.path.exists(save_folder):
            os.mkdir(save_folder)
            logging.info("Created folder %s", save_folder)
        else:
            logging.info("Folder %s already exists, continuing...", save_folder)


# TODO: theaded saving of clips, etc
# TODO: settings file or command line arg to set class variables instead of prompts
def main():
    no_prompt = False
    clip_save_folder = "clips"
    screenshot_save_folder = "screenshots"

    parser = argparse.ArgumentParser()
    parser.add_argument("--no-prompt", action='store_true', dest=no_prompt, help="Run the program without user prompts")
    # TODO: argument for settings file

    scraper = XboxScraper()
    scraper.user_prompts()

if __name__ == "__main__":
    main()


