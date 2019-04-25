class TextBlob():
    def __init__(self, *args, **kwargs):
        self.text = kwargs.get('text', '')

    def __eq__(self,other):
        return (self.text == other.text)

    def getText():
        return self.text

    def setText(text):
        self.text = text


class Review(TextBlob):
    def __init__(self, rating, *args, **kwargs):
        self.rating = rating
        self.comment = kwargs.get('comment', '')

    def __eq__(self,other):
        return (self.rating == other.rating 
        and )

    def getRating():
        return self.rating

    def setRating(rating):
        self.rating = rating

class Comment(TextBlob):
    def __init__(self, profile, *args, **kwargs):
        self.profile = profile
        super().__init__(self, *args, **kwargs)

    def 

class Description(TextBlob):
    pass
