from django.test import TestCase
from django.test import Client

class TestRunner(TestCase):
   c = Client()

   def test_main_view_get(self):
       get_response = self.c.get('/choices/')
       self.assertEqual(get_response.status_code,2011)

def runtests():
    runner = TestRunner()
    runner.test_main_view_get()
    
if __name__ == '__main__':
    runtests()
