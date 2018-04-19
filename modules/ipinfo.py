import requests


class IPinfo(object):
    def __init__(self, givenip=""):
        self.givenip = givenip
        self.ipwebsite = "https://ipinfo.io/"
        self.r = requests.get(self.ipwebsite + self.givenip)
        self.information = self.r.json()

    def ip(self):
        return self.information['ip']

    def hostname(self):
        return self.information['hostname']

    def loc(self):
        return self.information['loc']

    def org(self):
        return self.information['org']

    def city(self):
        return self.information['city']

    def region(self):
        return self.information['region']

    def country(self):
        return self.information['country']

    def phone(self):
        return self.information['phone']

    def allinfo(self):
        return self.information
