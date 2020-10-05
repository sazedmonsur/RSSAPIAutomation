import unittest
import GET_Request.FetchFeeds
from configparser import ConfigParser
import os

ft = GET_Request.FetchFeeds
config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../Config', 'config.ini'))


class MyTestCase(unittest.TestCase):

#Test to verify the response header values

    def test_response_header_server(self):
        self.assertEqual(ft.get_rss_headers(config['default']['root_url']).get("Server"), "Cowboy")

    def test_response_header_connection(self):
        self.assertEqual(ft.get_rss_headers(config['default']['root_url']).get("Connection"), "keep-alive")

    def test_response_header_X_Powered_By(self):
        self.assertEqual(ft.get_rss_headers(config['default']['root_url']).get("X-Powered-By"), "Express")

    def test_response_header_content_type(self):
        self.assertEqual(ft.get_rss_headers(config['default']['root_url']).get("Content-Type"),
                         "application/rss+xml; charset=utf-8")
