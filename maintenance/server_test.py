#!/usr/bin/python3
import unittest
import requests
class TestHttpService(unittest.TestCase):
    def test_refbase_homepage(self):
        r = requests.get('http://10.8.6.22:8084/')
        self.assertEqual(r.status_code, 200)
    def test_wiki_homepage(self):
        r = requests.get('http://10.8.6.22/wiki')
        self.assertEqual(r.status_code, 200)
    def test_gitlab_homepage(self):
        r = requests.get('http://10.8.6.22:88')
        self.assertEqual(r.status_code, 200)
    def test_nonexist(self):
        r = requests.get('http://10.8.6.22/non_exist')
        self.assertEqual(r.status_code, 404)

if __name__ == '__main__':
    unittest.main()