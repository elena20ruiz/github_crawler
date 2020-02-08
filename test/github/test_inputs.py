import unittest
from src.github import github
from src.errors import TypeOfError, InputError
from test import PROXIES
class TestInputForSearch(unittest.TestCase):

    def setUp(self):
        self.correct_type = 'Repositories'
        self.correct_keywords = ['js']
        self.correct_proxies = PROXIES
        self.correct_extra = False

    def test_correct_required_input(self):
        correct_data = {
            'keywords': self.correct_keywords,
            'type': self.correct_type,
            'proxies': self.correct_proxies
        }
        err, res = github.search(correct_data)
        self.assertFalse(err == TypeOfError.einput)

    def test_correct_all_parameters_input(self):
        correct_data = {
            'keywords': self.correct_keywords,
            'type': self.correct_type,
            'proxies': self.correct_proxies,
            'extra': self.correct_extra
        }
        err, res = github.search(correct_data)
        self.assertFalse(err.value == TypeOfError.einput)

    def test_incorrect_type(self):
        incorrect_type = {
            'keywords': self.correct_keywords,
            'type': 'wiki',
            'proxies': self.correct_proxies
        }
        err, res = github.search(incorrect_type)
        self.assertTrue(err == TypeOfError.einput)
        self.assertTrue(res == InputError.incorrect_type)

        incorrect_type['type'] = 1
        err, res = github.search(incorrect_type)
        self.assertTrue(err == TypeOfError.einput)
        self.assertTrue(res == InputError.bad_format_type)
    
    def test_incorrect_keywords(self):
        incorrect_keywords = {
            'keywords': "js",
            'type': self.correct_type,
            'proxies': self.correct_proxies
        }
        err, res = github.search(incorrect_keywords)
        self.assertTrue(err == TypeOfError.einput)
        self.assertTrue(res == InputError.bad_format_keywords)

        incorrect_keywords['keywords'] = [1, 2]
        err, res = github.search(incorrect_keywords)
        self.assertTrue(err == TypeOfError.einput)
        self.assertTrue(res == InputError.bad_format_keywords)

    def test_incorrect_proxies(self):
        incorrect_proxies = {
            'keywords': self.correct_keywords,
            'type': self.correct_type,
            'proxies': "123.123.123:5555"
        }
        err, res = github.search(incorrect_proxies)
        self.assertTrue(err == TypeOfError.einput)
        self.assertTrue(res == InputError.bad_format_proxies)

        incorrect_proxies['proxies'] = [1, 2]
        err, res = github.search(incorrect_proxies)
        self.assertTrue(err == TypeOfError.einput)
        self.assertTrue(res == InputError.bad_format_proxies)

    def test_incorrect_extra(self):
        incorrect_extra = {
            'keywords': self.correct_keywords,
            'type': self.correct_type,
            'proxies': self.correct_proxies,
            'extra': 'f'
        }
        
        err, res = github.search(incorrect_extra)
        self.assertTrue(err == TypeOfError.einput)
        self.assertTrue(res == InputError.bad_format_extra)

        incorrect_extra['extra'] = 1
        err, res = github.search(incorrect_extra)
        self.assertTrue(err == TypeOfError.einput)
        self.assertTrue(res == InputError.bad_format_extra)

    def test_missing_parameters(self):
        miss_keywords = {
            'type': self.correct_type,
            'proxies': self.correct_proxies,
            'extra': self.correct_extra
        }
        err, res = github.search(miss_keywords)
        self.assertTrue(err == TypeOfError.einput)
        self.assertTrue(res == InputError.missing_parameter)

        miss_type = {
            'keywords': self.correct_keywords,
            'proxies': self.correct_proxies,
            'extra': self.correct_extra
        }
        err, res = github.search(miss_type)
        self.assertTrue(err == TypeOfError.einput)
        self.assertTrue(res == InputError.missing_parameter)

        miss_proxies = {
            'keywords': self.correct_keywords,
            'type': self.correct_type,
            'extra': self.correct_extra
        }
        err, res = github.search(miss_proxies)
        self.assertTrue(err == TypeOfError.einput)
        self.assertTrue(res == InputError.missing_parameter)