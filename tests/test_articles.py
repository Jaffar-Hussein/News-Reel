import unittest
from models import articles

Article=articles.Articles

class TestArticles(unittest.TestCase):
    """
    The test for the articles class

    Args:
        unittest : The unittest
    """
    def setUp(self):
        """
        This is the set up that runs before the test
        """
        self.new_article= Article('Hanan','The cries of the modern man','Long description ...','https//www.image.jpg','https://www.image.jpg','22-11-02')
        
    def test_news_source_(self):
        """
        Test if the instance created by article class
        """
        self.assertTrue(isinstance(self.new_article,Article))
        
if __name__ == '__main__':
    unittest.main()