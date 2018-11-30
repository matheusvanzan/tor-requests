import requests
import tor_requests
import json
import unittest


URL = 'https://api.ipify.org?format=json'


class TypeTest(unittest.TestCase):
    
    def test(self):
        s1 = requests.session()
        self.assertEqual(type(s1), requests.sessions.Session)
        
        s2 = tor_requests.session()
        self.assertEqual(type(s2), tor_requests.sessions.Session)
        
        
class ValueTest(unittest.TestCase):
    
    def test(self):
        s1 = requests.session()
        r1 = s1.get(URL)
        ip1 = json.loads(r1.text)['ip']
        
        s2 = tor_requests.session()
        r2 = s2.get(URL)
        ip2 = json.loads(r2.text)['ip']
        self.assertNotEqual(ip1, ip2)


if __name__ == '__main__':
    unittest.main()