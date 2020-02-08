import unittest, time
from src.github import github
from src.errors import TypeOfError, RequestError
from test import PROXIES
class TestSimpleSearch(unittest.TestCase):

    def setUp(self):
        self.correct_input1 = {
            'type': 'Repositories',
            'keywords': ["openstack", "nova", "css"],
            'proxies': PROXIES,
            'extra': True
        }

        self.correct_input2 = {
            'type': 'Repositories',
            'keywords': [ "python", "django-rest-framework", "jwt"],
            'proxies': PROXIES,
            'extra': True
        }

        self.expected_result1 = [
            {
                "extra": {
                    "language_stats": {
                        "CSS": 52.0,
                        "HTML": 0.8,
                        "JavaScript": 47.2
                    },
                    "owner": "atuldjadhav"
                },
                "url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage"
            },
            {
                "extra": {
                    "language_stats": {
                        "Python": 100.0
                    },
                    "owner": "michealbalogun"
                },
                "url": "https://github.com/michealbalogun/Horizon-dashboard"
            }
        ]

        self.expected_result2 = [
            {
                "extra": {
                    "language_stats": {
                        "Python": 100.0
                    },
                    "owner": "always-awake"
                },
                "url": "https://github.com/always-awake/SideProject_4"
            },
            {
                "extra": {
                    "language_stats": {
                        "HTML": 2.3,
                        "Python": 97.7
                    },
                    "owner": "Firok"
                },
                "url": "https://github.com/Firok/RestApp"
            },
            {
                "extra": {
                    "language_stats": {
                        "Python": 75.6,
                        "Shell": 24.4
                    },
                    "owner": "antonioxtasis"
                },
                "url": "https://github.com/antonioxtasis/Django2_API"
            },
            {
                "extra": {
                    "language_stats": {
                        "Python": 100.0
                    },
                    "owner": "danagar0312"
                },
                "url": "https://github.com/danagar0312/heroku-hyle-proj"
            },
            {
                "extra": {
                    "language_stats": {
                        "Python": 100.0
                    },
                    "owner": "Rabia23"
                },
                "url": "https://github.com/Rabia23/DjangoRestJWTAuthentication"
            },
            {
                "extra": {
                    "language_stats": {
                        "Python": 100.0
                    },
                    "owner": "vaibhavkollipara"
                },
                "url": "https://github.com/vaibhavkollipara/ChatroomApi"
            },
            {
                "extra": {
                    "language_stats": {
                        "CSS": 54.3,
                        "HTML": 0.1,
                        "JavaScript": 18.8,
                        "Vue": 26.8
                    },
                    "owner": "zhaorch"
                },
                "url": "https://github.com/zhaorch/shanks-vue"
            }
        ]

    def test_correct_search(self):
        err, res = github.search(self.correct_input1)
        self.assertTrue(err == TypeOfError.none)
        self.assertTrue(res == self.expected_result1)
        time.sleep(1)
        err, res = github.search(self.correct_input2)
        self.assertTrue(err == TypeOfError.none)
        self.assertTrue(res == self.expected_result2)

    def test_timeout_bad_proxy(self):
        self.correct_input1['proxies'] = ['1.12.124.332:3322']
        err, res = github.search(self.correct_input1)
        self.assertTrue(err == TypeOfError.erequest)
        self.assertTrue(res == RequestError.timeout)
        