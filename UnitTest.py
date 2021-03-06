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
        self.permA = User.Permission('test', view=True)
        self.permB = User.Permission('test')
        self.permC = User.Permission('test')
        self.permD = User.Permission('new')
        
        self.profA = User.Profile(permissions = [self.permA])
        self.profB = User.Profile(permissions = [self.permB])
        self.profC = User.Profile(permissions = [self.permC])
        self.profD = User.Profile(permissions = [self.permC])

        self.commentA = TextBlobs.Comment(self.profA, text='I am Comment')
        self.commentB = TextBlobs.Comment(self.profC, text='I am diff Comment')

        self.composerA = User.Composer('admin', 'passwd')
        self.composerB = User.Composer('admin', 'no')
        self.composerC = User.Composer('user', 'asdfg')

        self.compositionA = Composition.Composition(description = TextBlobs.Description(text='test'))
        self.reviewA = TextBlobs.Review(7, comment=self.commentA)

    def testPermissionEquals(self):
        self.assertTrue(self.permA != self.permB)
        self.assertTrue(self.permB == self.permC)
    
    def testPermissionEdit(self):
        self.assertTrue(self.permA.getEdit() == False)
        self.permA.setEdit(True)
        self.assertTrue(self.permA.getEdit() == True)
    
    def testPermissionView(self):
        self.assertTrue(self.permA.getView() == True)
        self.permA.setView(False)
        self.assertTrue(self.permA.getView() == False)
    
    def testPermissionShare(self):
        self.assertTrue(self.permA.getShare() == False)
        self.permA.setShare(True)
        self.assertTrue(self.permA.getShare() == True)
    

    def testPermissionName(self):
        self.assertTrue(self.permA.getName() == 'test')
        self.assertTrue(self.permA.getName() != 'new')
    
    def testProfileEquals(self):
        self.profB.addComment(self.commentA)
        self.profC.addComment(self.commentA)
        self.assertTrue(self.profB == self.profC)
        self.profC.addComment(self.commentB)
        self.assertFalse(self.profB == self.profC)

    def testProfilePermission(self):
        self.assertTrue(self.permA in self.profA.getPermissions())
        self.assertTrue(self.permD not in self.profA.getPermissions())
        self.profA.addPermission(self.permD)
        self.assertTrue(self.permD in self.profA.getPermissions())
        self.profA.deletePermission(self.permA)
        self.assertTrue(self.permA not in self.profA.getPermissions())

    def testProfileComments(self):
        self.assertTrue(self.commentA not in self.profA.getComments())
        self.profA.addComment(self.commentA)
        self.assertTrue(self.commentA in self.profA.getComments())
        self.profA.deleteComment(self.commentA)
        self.assertTrue(self.commentA not in self.profA.getComments())

    def testComposerEquals(self):
        self.assertTrue(self.composerA == self.composerB)
        self.assertTrue(self.composerA != self.composerC)
    
    def testComposerUsername(self):
        self.assertTrue(self.composerA == self.composerB)
        self.assertTrue(self.composerA != self.composerC)

    def testComposerPassword(self):
        self.assertTrue(self.composerA.getPassword() == 'passwd')
    
    def testComposerProfile(self):
        self.assertTrue(self.composerA.getProfile() == None)
        self.composerA.setProfile(self.profA)
        self.assertTrue(self.composerA.getProfile() == self.profA)
    
    def testComposerCompositions(self):
        self.assertTrue(self.compositionA not in self.composerA.getCompositions())
        self.composerA.addComposition(self.compositionA)
        self.assertTrue(self.compositionA in self.composerA.getCompositions())
        self.composerA.deleteComposition(self.compositionA)
        self.assertTrue(self.compositionA not in self.composerA.getCompositions())

    def testComposerReviews(self):
        self.assertTrue(self.reviewA not in self.composerA.getReviews())
        self.composerA.addReview(self.reviewA)
        self.assertTrue(self.reviewA in self.composerA.getReviews())
        self.composerA.deleteReview(self.reviewA)
        self.assertTrue(self.reviewA not in self.composerA.getReviews())

    def tearDown(self):
        pass

class TestComposition(unittest.TestCase):
    def setUp(self):
        self.simpleInstrument = Composition.Instrument('kittens', 'BackEnd/WavInstrument/cat_kitten.wav')
        self.simpleNote = Composition.Note(instrument = self.simpleInstrument)
        self.quarterNote = Composition.Note(instrument = self.simpleInstrument, duration=1/4)
        self.simpleMeasure = Composition.Measure(Composition.Note(instrument = self.simpleInstrument, startingBeat = 0, duration = 1/4)) 
        self.simpleComposition = Composition.Composition(description = TextBlobs.Description(text='I am a simple description'))
    
    def testNoteGetInstrument(self):
        self.assertEqual(self.simpleNote.getInstrument(), self.simpleInstrument)

    def testNoteSetInstrument(self):
        self.assertEqual(self.simpleNote.getInstrument(), self.simpleInstrument)
        self.simpleNote.setInstrument(None)
        self.assertEqual(self.simpleNote.getInstrument(), None)

    def testNoteGetFrequency(self):
        self.assertEqual(self.simpleNote.getFrequency(), None)

    def testNoteSetFrequency(self):
        self.assertEqual(self.simpleNote.getFrequency(), None)
        self.simpleNote.setFrequency(21)
        self.assertEqual(self.simpleNote.getFrequency(), 21)

    def testNoteGetStartingBeat(self):
        self.assertEqual(self.simpleNote.getStartingBeat(), None)

    def testNoteSetStartingBeat(self):
        self.assertEqual(self.simpleNote.getStartingBeat(), None)
        self.simpleNote.setStartingBeat(1/16)
        self.assertEqual(self.simpleNote.getStartingBeat(), 1/16)

    def testNoteGetDuration(self):
        self.assertEqual(self.simpleNote.getDuration(), None)

    def testNoteSetDuration(self):
        self.assertEqual(self.simpleNote.getDuration(), None)
        self.simpleNote.setDuration(1/4)
        self.assertEqual(self.simpleNote.getDuration(), 1/4)

    def testNoteGetLetter(self):
        self.simpleNote.setFrequency(21)
        self.assertEqual(self.simpleNote.getNoteLetter(), ('E', 0))
    
    def testMeasureGetKeySignature(self):
        self.assertEqual(self.simpleMeasure.getKeySignature(), None)

    def testMeasureSetKeySignature(self):
        self.assertEqual(self.simpleMeasure.getKeySignature(), None)
        self.simpleMeasure.setKeySignature(('C', 'flat', 'major'))
        self.assertEqual(self.simpleMeasure.getKeySignature(), ('C', 'flat', 'major'))

    def testMeasureGetTimeSignature(self):
        self.assertEqual(self.simpleMeasure.getTimeSignature(), None)

    def testMeasureSetTimeSignature(self):
        self.assertEqual(self.simpleMeasure.getTimeSignature(), None)
        self.simpleMeasure.setTimeSignature(3/4)
        self.assertEqual(self.simpleMeasure.getTimeSignature(), 3/4)

    def testMeasureAddNote(self):
        self.simpleMeasure.setTimeSignature(3/4)
        self.assertEqual(len(self.simpleMeasure.notes), 0)
        self.simpleMeasure.addNote(self.quarterNote)
        self.simpleMeasure.addNote(self.quarterNote)
        self.simpleMeasure.addNote(self.quarterNote)
        self.assertEqual(self.simpleMeasure.notesDuration, 3/4)
        self.simpleMeasure.addNote(self.quarterNote)
        self.assertEqual(self.simpleMeasure.notesDuration, 3/4)

    def testMeasureRemoveNote(self):
        self.simpleMeasure.setTimeSignature(3/4)
        self.assertEqual(len(self.simpleMeasure.notes), 0)
        self.simpleMeasure.addNote(self.quarterNote)
        self.simpleMeasure.removeNote(self.quarterNote)
        self.assertEqual(len(self.simpleMeasure.notes), 0)
    
    def testCompositionAddMeasure(self):
        self.assertEqual(len(self.simpleComposition.getMeasures()), 0)
        self.simpleComposition.addMeasure(self.simpleMeasure)
        self.assertEqual(len(self.simpleComposition.getMeasures()), 1)

    def testCompositionDeleteMeasure(self):
        self.assertEqual(len(self.simpleComposition.getMeasures()), 0)
        self.simpleComposition.addMeasure(self.simpleMeasure)
        self.assertEqual(len(self.simpleComposition.getMeasures()), 1)
        self.simpleComposition.deleteMesure(self.simpleMeasure)
        self.assertEqual(len(self.simpleComposition.getMeasures()), 0)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()