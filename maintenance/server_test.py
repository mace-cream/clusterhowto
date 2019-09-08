#!/usr/bin/python3
import unittest
import requests
class TestHttpService(unittest.TestCase):
    def test_refbase_homepage(self):
        r = requests.get('http://10.8.4.170:8084/')
        self.assertEqual(r.status_code, 200)
    def test_wiki_homepage(self):
        r = requests.get('http://10.8.4.170/wiki')
        self.assertEqual(r.status_code, 200)
    def test_gitlab_homepage(self):
        r = requests.get('http://10.8.4.170:88')
        self.assertEqual(r.status_code, 200)
    def test_nonexist(self):
        r = requests.get('http://10.8.4.170/non_exist')
        self.assertEqual(r.status_code, 404)

if __name__ == '__main__':
    unittest.main()