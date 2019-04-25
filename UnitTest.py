"""
"""

import unittest
import BackEnd.User as User
import BackEnd.TextBlobs as TextBlobs
import BackEnd.Composition as Composition
import BackEnd.Music as Music

class TestTextBlobs(unittest.TestCase):
    def setUp(self):
        self.emptyBlob = TextBlobs.TextBlob()
        self.fullBlob = TextBlobs.TextBlob(text='I am Text')
        self.fullDesc = TextBlobs.Description(text='I am Description')
        baseProfile = User.Profile()
        self.emptyComment = TextBlobs.Comment(baseProfile)
        self.fullComment = TextBlobs.Comment(baseProfile, text='I am Comment')
        self.identicalComment = TextBlobs.Comment(baseProfile, text='I am Comment')
        self.diffComment = TextBlobs.Comment(baseProfile, text='I am diff Comment')
        self.diffProfComment = TextBlobs.Comment(User.Profile(User.Composer('Otherusername', 'password')), text='I am Comment')
        self.fullReview = TextBlobs.Review(7, comment='I am Review')
        self.identicalReview = self.fullReview = TextBlobs.Review(7, comment='I am Review')
        self.diffReview = TextBlobs.Review(7, comment = 'I am diff Review')
        self.diffRateReview =TextBlobs.Review(8, comment='I am Review')

    def testGetText(self):
        self.assertEqual(self.emptyBlob.getText(), '')
        self.assertEqual(self.fullBlob.getText(), 'I am Text')
    
    def testBlobEquals(self):
        self.assertTrue(self.emptyBlob == self.emptyBlob)
        self.assertTrue(self.emptyBlob != self.fullBlob)

    def testReviewEquals(self):
        self.assertTrue(self.fullReview == self.fullReview)
        self.assertTrue(self.fullReview == self.identicalReview)
        self.assertTrue(self.fullReview != self.diffReview)
        self.assertTrue(self.fullReview != self.diffRateReview)

    def testComentEquals(self):
        self.assertTrue(self.fullComment == self.fullComment)
        self.assertTrue(self.fullComment == self.identicalComment)
        self.assertTrue(self.fullComment != self.diffComment)
        self.assertTrue(self.fullComment != self.diffProfComment)

    def tearDown(self):
        pass


class TestUser(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

class TestComposition(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

class TestMusic(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()