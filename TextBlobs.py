class TextBlob():
    def __init__(self, *args, **kwargs):
        self.text = kwargs.get('text', '')

    def __eq__(self,other):
        return (self.text == other.text)

    def getText():
        return self.text

    def setText(text):
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

    def getProfile():
        return self.profile

class Review():
    def __init__(self, rating, *args, **kwargs):
        self.rating = rating
        self.comment = kwargs.get('comment', '')

    def __eq__(self,other):
        return (self.rating == other.rating 
        and self.comment == other.comment)

    def getRating():
        return self.rating

    def setRating(rating):
        self.rating = rating

    def getComment():
        return self.comment

    def setComment(comment):
        self.comment = comment

