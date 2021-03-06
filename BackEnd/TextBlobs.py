"""
AUTHOR: Virginia Tech Lacrosse Team

Functionality for storing and manipulating text information

DIFFERENCES FROM CLASS DIAGRAM:

__eq__ methods added across each of the classes to allow for comparison
Overloaded Constructors accomplished through python's kwargs system
(you can pass in a variable number of keyworded arguments)

TextBlob:
    gt added to enable sorting
    
Review:
    Review No Longer inherits from TextBlob, it only needs to store a comment
"""

class TextBlob():
    def __init__(self, *args, **kwargs):
        self.text = kwargs.get('text', '')

    def __eq__(self,other):
        return (self.text == other.text)

    def __gt__(self, other):
        return self.text > other.text

    def getText(self):
        return self.text

    def setText(self, text):
        self.text = text

class Description(TextBlob):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def __eq__(self,other):
        return super().__eq__(self, other)

class Comment(TextBlob):
    def __init__(self, profile, *args, **kwargs):
        self.profile = profile
        super().__init__(self, *args, **kwargs)

    def __eq__(self, other):
        return (self.profile == other.profile
        and self.text == other.text)

    def getProfile(self):
        return self.profile

class Review():
    def __init__(self, rating, *args, **kwargs):
        self.rating = rating
        self.comment = kwargs.get('comment', '')

    def __eq__(self,other):
        return (self.rating == other.rating 
        and self.comment == other.comment)

    def getRating(self):
        return self.rating

    def setRating(self, rating):
        self.rating = rating

    def getComment(self):
        return self.comment

    def setComment(self, comment):
        self.comment = comment

