import unittest
import pandas as pd
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def setUp(self):
        self.test_object = BookLover("riya pulla", "riya@pulla.com", "dystopian")
    
    def test_1_add_book(self):
        self.test_object.add_book("percy jackson", 4)
        self.assertTrue(self.test_object.has_read("percy jackson"))
    
    def test_2_add_book(self):
        self.test_object.add_book("percy jackson", 4)
        self.test_object.add_book("percy jackson", 4)
        self.assertEqual(len(self.test_object.book_list), 1)
    
    def test_3_has_read(self):
        self.test_object.add_book("percy jackson", 4)
        self.assertTrue(self.test_object.has_read("percy jackson"))
    
    def test_4_has_read(self):
        self.assertFalse(self.test_object.has_read("giver"))
    
    def test_5_num_books_read(self):
        self.test_object.add_book("percy jackson", 4)
        self.test_object.add_book("giver", 5)
        self.assertEqual(self.test_object.num_books_read(), 2)
    
    def test_6_fav_books(self):
        self.test_object.add_book("percy jackson", 4)
        self.test_object.add_book("giver", 5)
        favs = self.test_object.fav_books()
        self.assertTrue(all(favs['book_rating'] > 3))
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
