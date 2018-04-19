"""Module to test for IPInfo class."""
import unittest
from modules.ipinfo import IPinfo


class TestIPInfo(unittest.TestCase):
    """Test for IPInfo class and features."""

    def setUp(self):
        """Set up global variables."""
        self.givenip = '8.8.8.8'
        self.ipinfo = IPinfo(self.givenip)

    def test_ipinfo_attributes(self):
        """Test IPInfo attributes."""
        self.assertEqual(self.ipinfo.ip, '8.8.8.8')
        self.assertEqual(self.ipinfo.hostname,
                         'google-public-dns-a.google.com')
        self.assertEqual(self.ipinfo.loc, '37.3860,-122.0840')
        self.assertEqual(self.ipinfo.org, 'AS15169 Google LLC')
        self.assertEqual(self.ipinfo.city, 'Mountain View')
        self.assertEqual(self.ipinfo.country, 'US')
        self.assertEqual(self.ipinfo.region, 'California')
        self.assertEqual(self.ipinfo.phone, '650')
