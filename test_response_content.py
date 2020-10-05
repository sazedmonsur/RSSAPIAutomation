import unittest
from time import sleep

import GET_Request.FetchFeeds
from datetime import datetime
from configparser import ConfigParser
import os


ft = GET_Request.FetchFeeds

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../Config', 'config.ini'))
now = datetime.now().utcnow()

class MyTestCase(unittest.TestCase):

#Test to verify default number of items in the feed
    def test_default_feed_number_of_entries_should_be_10(self):
        self.assertEqual(ft.get_default_feed_number_of_items(), 10)

#Test to verify current build time
    def test_current_build_time_verification(self):
        self.assertEqual(ft.get_current_build_time_in_minutes(), now.strftime("%M"))

#Test to verify build time updates every seconds
    def test_build_time_updates_every_second(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'second'}
        current_build_time = ft.get_build_time_in_seconds(param1, param2)
        sleep(1)
        build_time_after_1_sec = ft.get_build_time_in_seconds(param1, param2)
        self.assertNotEqual(current_build_time, build_time_after_1_sec)