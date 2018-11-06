from django.test import TestCase
from django.test import Client

class TestRunner(TestCase):
   def test_main_view_get(self):
       c = Client()
       get_response = c.get('/choices/')
       self.assertEqual(get_response.status_code,2011)

def runtests():
    TestRunner()
    
if __name__ == '__main__':
    runtests()
