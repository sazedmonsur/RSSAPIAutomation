import os
import unittest
from configparser import ConfigParser


import GET_Request.FetchFeeds

ft = GET_Request.FetchFeeds
config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../Config', 'config.ini'))


class MyTestCase(unittest.TestCase):
    def test_response_code_for_valid_url_should_be_200(self):
        self.assertEqual(ft.get_rss_feed_response_code_url(config['default']['root_url']), 200)

    def test_response_code_for_invalid_url_should_be_404(self):
        self.assertEqual(ft.get_rss_feed_response_code_url(config['default']['invalid_url']), 404)

    def test_response_code_for_invalid_param_should_be_500(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'seconds'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 500)

    def test_response_code_for_unit_second_should_be_200(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'second'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 200)

    def test_response_code_for_unit_minute_should_be_200(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'minute'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 200)

    def test_response_code_for_unit_month_should_be_200(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'month'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 200)

    def test_response_code_for_unit_day_should_be_200(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'day'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 200)

    def test_response_code_for_unit_second_and_valid_interval_should_be_200(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'second', 'interval': '30'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 200)

    def test_response_code_for_unit_second_and_invalid_interval_should_be_500(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'second', 'interval': '600'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 500)

    def test_response_code_for_unit_minute_and_valid_interval_should_be_200(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'minute', 'interval': '6'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 200)

    def test_response_code_for_unit_minute_and_invalid_interval_should_be_500(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'minute', 'interval': '9'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 500)

    def test_response_code_for_unit_day_and_valid_interval_should_be_200(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'day', 'interval': '1'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 200)

    def test_response_code_for_unit_day_and_invalid_interval_should_be_500(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'day', 'interval': '9'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 500)

    def test_response_code_for_unit_month_and_valid_interval_should_be_200(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'month', 'interval': '1'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 200)

    def test_response_code_for_unit_month_and_invalid_interval_should_be_500(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'month', 'interval': '5'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 500)

    def test_response_code_for_unit_year_and_valid_interval_should_be_200(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'year', 'interval': '1'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 200)

    def test_response_code_for_unit_year_and_invalid_interval_should_be_500(self):
        param1 = config['default']['root_url']
        param2 = params = {'unit': 'year', 'interval': '9'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 500)

    def test_response_code_for_valid_length_should_be_200(self):
        param1 = config['default']['root_url']
        param2 = params = {'length': '5'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 200)

    def test_response_code_for_invalid_length_should_be_500(self):
        param1 = config['default']['root_url']
        param2 = params = {'length': '-5'}
        self.assertEqual(ft.get_rss_feed_response_code_url_with_unit(param1, param2), 500)
