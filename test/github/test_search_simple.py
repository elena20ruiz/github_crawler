import unittest
from src.github import github
from src.errors import TypeOfError, RequestError

class TestSimpleSearch(unittest.TestCase):

    def setUp(self):
        self.correct_input1 = {
            'type': 'Repositories',
            'keywords': ["openstack", "nova", "css"],
            'proxies': ['178.128.233.79:8118','109.199.77.83:41138','186.46.3.238:46849	']
        }

        self.correct_input2 = {
            'type': 'Repositories',
            'keywords': [ "python", "django-rest-framework", "jwt"],
            'proxies': ['178.128.233.79:8118','109.199.77.83:41138','186.46.3.238:46849	']
        }

        self.expected_result1 = [
            {
                "url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage"
            },
            {
                "url": "https://github.com/michealbalogun/Horizon-dashboard"
            }
        ]

        self.expected_result2 = [
            {
                "url": "https://github.com/always-awake/SideProject_4"
            },
            {
                "url": "https://github.com/Firok/RestApp"
            },
            {
                "url": "https://github.com/antonioxtasis/Django2_API"
            },
            {
                "url": "https://github.com/danagar0312/heroku-hyle-proj"
            },
            {
                "url": "https://github.com/Rabia23/DjangoRestJWTAuthentication"
            },
            {
                "url": "https://github.com/vaibhavkollipara/ChatroomApi"
            },
            {
                "url": "https://github.com/zhaorch/shanks-vue"
            }
        ]

    def test_correct_search(self):
        err, res = github.search(self.correct_input1)
        self.assertTrue(err == TypeOfError.none)
        self.assertTrue(res == self.expected_result1)

        err, res = github.search(self.correct_input2)
        self.assertTrue(err == TypeOfError.none)
        self.assertTrue(res == self.expected_result2)

    def test_timeout_bad_proxy(self):
        self.correct_input1['proxies'] = ['1.12.124:3322']
        err, res = github.search(self.correct_input1)
        self.assertTrue(err == TypeOfError.erequest)
        self.assertTrue(res == RequestError.timeout)