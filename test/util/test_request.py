import unittest
from src.util import request as r

class TestInputForSearch(unittest.TestCase):

    def setUp(self):
        self.correct_url= 'https://ecosia.org/search'
        self.correct_param = {'q': 'search'}
        self.correct_proxy = ['179.252.97.60:80']

    def test_correct_request(self):

        req = r.make_request(self.correct_url, self.correct_param, None)
        self.assertTrue(req.status_code == 200)
        self.assertTrue(req.content)

    def test_invalid_url_request(self):
        req = r.make_request('23mdskakak', self.correct_param, self.correct_proxy )
        self.assertTrue(req == None)
    
    def test_no_proxy(self):
        req = r.make_request(self.correct_url, self.correct_param, None )
        self.assertTrue(req.status_code == 200)
        self.assertTrue(req.content)