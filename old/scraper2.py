__author__ = 'Tehlizard'

import requests
import json


# The class structure is based off of the python wrapper written by voidpirate
# Github: https://github.com/xboxapi/Python-Wrapper/blob/master/xboxapi/xbox_api.py
class XboxApi:
    # API key
    # Set this on program initialization
    api_key = ""
    xuid = ""

    def __init__(self, api_key):
        self.api_key = api_key

    def get_user_profile(self, xuid):
        res = self.request("https://xboxapi.com/v2/{}/profile".format(xuid))
        return res.json()

    def get_user_gamercard(self, xuid):
        res = self.request("https://xboxapi.com/v2/{}/gamercard".format(xuid))
        return res.json()

    def get_profile(self):
        """Return information for current token profile"""
        res = self.request("https://xboxapi.com/v2/profile")
        return res.json()

    def get_xuid(self):
        """Return your xuid"""
        res = self.request("https://xboxapi.com/v2/accountXuid")
        return res.json()

    def get_messages(self):
        """Return your messages"""
        res = self.request("https://xboxapi.com/v2/messages")
        return res.json()

    def get_conversations(self):
        """Return your messages"""
        res = self.request("https://xboxapi.com/v2/conversations")
        return res.json()

    def get_all_clips(self):
        res = self.request("https://xboxapi.com/v2/{" + xuid + "}/game-clips")
        return res.json()

    def get_game_clips(self, game_title):
        res = self.request("https://xboxapi.com/v2/{" + xuid + "}/game-clips/" + game_title)
        return res.json()

    def get_screenshots(self):
        res = self.request("https://xboxapi.com/v2/{" + xuid + "}/screenshots")
        return res.json()

    def get_game_screenshots(self, game_title):
        res = self.request("https://xboxapi.com/v2/{" + xuid + "}/screenshots/" + game_title)
        return res.json()

    


    # TODO: checks for failed requests
    def resolve_xuid(self):
        json_data = self.get_xuid()
        parsed_data = json.loads(json_data)
        xuid = parsed_data["xuid"]

    def send_message(self, message, xuids=[]):
        """Send a message to a set of user(s)"""
        headers = {
                    "X-AUTH" : self.api_key,
                    "Content-Type" : "application/json"
                  }

        payload = {
            "message" : message,
            "to" : []
        }

        for xuid in xuids:
            payload["to"].append(xuid)

        res = requests.post("https://xboxapi.com/v2/messages", headers=headers, data=json.dumps(payload))
        res.json()

    def request(self, url):
        """Wrapper on the requests.get"""
        headers = {"X-AUTH" : self.api_key}
        res = requests.get(url, headers=headers)
        return res

