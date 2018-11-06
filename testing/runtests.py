from django.test import TestCase

class TestRunner(TestCase):
   def test_0(self):
       self.assertEqual(0-0, 0+0)

def runtests():
    TestRunner()
    
if __name__ == '__main__':
    runtests()
