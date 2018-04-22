import requests


class IPinfo(object):
    def __init__(self, givenip=""):
        self.givenip = givenip
        self.ipwebsite = "https://ipinfo.io/"
        self.r = requests.get(self.ipwebsite + self.givenip)
        self.information = self.r.json()
        self.ip = self.information["ip"]
        self.hostname = self.information["hostname"]
        self.city = self.information["city"]
        self.region = self.information["region"]
        self.county = self.information["county"]
        self.loc = self.information["loc"]
        self.org = self.information["org"]
