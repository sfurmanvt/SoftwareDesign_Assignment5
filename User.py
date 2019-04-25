class Permission(): 
    def __init__(self, name):
        self.name = name
        self.canEdit = False
        self.canView = False
        self.canShare = False

    def __eq__(self, other):
        return (self.name == other.name
        and self.canEdit == other.canEdit
        and self.canView == other.canEdit
        and self.canShare == other.canShare)

class Profile():
    def __init__(self, composer, *args, **kwargs):
        self.composer = composer
        self.permissions = kwargs.get('permissions', [])
        self.comments = kwargs.get('comments', [])
        
    def __eq__(self, other):
        return (self.composer == other.composer
        and sorted(self.permissions) == sorted(other.permissions)
        and sorted(self.comments) == sorted(other.comments))

    def addPermission(permission):
        self.permissions = permission

    def deletePermission(permission):
        if permission in self.permissions:
            self.premissions.remove(permission)

    def addComment(comment):
        self.comment.append(comment)

    def deleteComment(comment):
        if comment in self.comments:
            self.coments.remove(comment)
    
    def getComposer():
        return self.composer

class Composer():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.profile = None
        self.compositions = []
        self.reviews = [] 
    
    def __eq__(self, other):
        return (self.username == other.username
        and self.password == other.password
        and self.profile == other.profile
        and sorted(self.compositions) == sorted(other.compositions)
        and sorted(self.reviews) == sorted(other.reviews))


    def getUsername():
        return self.username
    
    def getPassword():
        return self.password

    def getProfile():
        return self.profile

    def setProfile(profile):
        self.profile = profile

    def addComposition(composition):
        compositions.append(composition)

    def deleteComposition(composition):
        if delComposition in self.compositions:
            self.compositions.remove(composition)

    def addReview(review):
        reviews.append(review)
    
    def deleteReview(review):
        if review in self.reviews:
            self.reviews.remove(review)
