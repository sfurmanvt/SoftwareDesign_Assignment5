"""
AUTHOR: Virginia Tech Lacrosse Team

25 Unit tests for our backend methods
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
        self.diffProfComment = TextBlobs.Comment(User.Profile(permissions = [User.Permission('name')]), text='I am Comment')
        self.fullReview = TextBlobs.Review(7, comment=self.fullComment)
        self.identicalReview = self.fullReview = TextBlobs.Review(7, comment=self.fullComment)
        self.diffReview = TextBlobs.Review(7, comment = self.diffComment)
        self.diffRateReview =TextBlobs.Review(8, comment=self.fullComment)

    def testGetText(self):
        self.assertEqual(self.emptyBlob.getText(), '')
        self.assertEqual(self.fullBlob.getText(), 'I am Text')
    
    def testBlobEquals(self):
        self.assertTrue(self.emptyBlob == self.emptyBlob)
        self.assertTrue(self.emptyBlob != self.fullBlob)

    def testComentEquals(self):
        self.assertTrue(self.fullComment == self.fullComment)
        self.assertTrue(self.fullComment == self.identicalComment)
        self.assertTrue(self.fullComment != self.diffComment)
        self.assertTrue(self.fullComment != self.diffProfComment)

    def testCommentGetProfile(self):
        self.assertEqual(self.emptyComment.getProfile(), User.Profile())
        self.assertEqual(self.fullComment.getProfile(), User.Profile())

    def testReviewEquals(self):
        self.assertTrue(self.fullReview == self.fullReview)
        self.assertTrue(self.fullReview == self.identicalReview)
        self.assertTrue(self.fullReview != self.diffReview)
        self.assertTrue(self.fullReview != self.diffRateReview)

    def testReviewGetRating(self):
        self.assertEqual(self.fullReview.getRating(), 7)
        self.assertEqual(self.diffRateReview.getRating(), 8)

    def testReviewSetRating(self):
        self.assertEqual(self.fullReview.getRating(), 7)
        self.fullReview.setRating(9)
        self.assertEqual(self.fullReview.getRating(), 9)

    def reviewGetComment(self):
        self.assertEqual(self.fullReview.getComment(), self.identicalComment)

    def reviewSetComment(self):
        self.assertEqual(self.fullReview.getComment(), self.identicalComment)
        self.fullReview.setComment(self.diffComment)
        self.assertEqual(self.fullReview.getComment(), self.diffComment)

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