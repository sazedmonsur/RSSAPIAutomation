from time import sleep

import requests
from configparser import ConfigParser
from xml.etree import ElementTree
import os

#parsing from the config file
config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../Config', 'config.ini'))

response = requests.get(config['default']['root_url'])

#parsing the XML response
tree = ElementTree.fromstring(response.content)

#response code for a GET request without parameters
def get_rss_feed_response_code_url(url):
    return requests.get(url).status_code

#response code for a GET request with parameters
def get_rss_feed_response_code_url_with_unit(url, param1):
    return requests.get(url, param1).status_code

#to get the while content of the response
def get_rss_feed_content(url):
    return requests.get(url).content

#to get the headers value of the response
def get_rss_headers(url):
    return requests.get(url).headers

#to get the default numbers of items in the response feed
def get_default_feed_number_of_items():
    count = 0
    for item in tree.iter('item'):
        count += 1
    return count

#to get the current build time in minutes
def get_current_build_time_in_minutes():
    for buildtime in tree.iter('lastBuildDate'):
        return buildtime.text[20:22]

#to get the current build time in seconds
def get_build_time_in_seconds(url, param1):
    tree_param = ElementTree.fromstring(requests.get(url,param1).content)
    for buildtime in tree_param.iter('lastBuildDate'):
        return buildtime.text[23:25]