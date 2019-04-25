"""
AUTHOR: Virginia Tech Lacrosse Team

Functionality for storing and manipulating compositions

DIFFERENCES FROM CLASS DIAGRAM:

"""

class Permission(): 
    def __init__(self, name, edit=False, view=False, share=False):
        self.name = name
        self.canEdit = edit
        self.canView = view
        self.canShare = share

    def __eq__(self, other):
        return (self.name == other.name
        and self.canEdit == other.canEdit
        and self.canView == other.canEdit
        and self.canShare == other.canShare)

    def __gt__(self, other):
        return self.name > other.name

    def setEdit(self, value):
        self.canEdit = value
    
    def getEdit(self):
        return self.canEdit
    
    def setView(self, value):
        self.canView = value
    
    def getView(self):
        return self.canView
    
    def setShare(self, value):
        self.canShare = value
    
    def getShare(self):
        return self.canShare
    
    def getAll(self):
        return (self.canEdit, self.canView, self.canShare)

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

class Profile():
    def __init__(self, *args, **kwargs):
        self.permissions = kwargs.get('permissions', [])
        self.comments = []
        
    def __eq__(self, other):
        return (sorted(self.permissions) == sorted(other.permissions)
        and sorted(self.comments) == sorted(other.comments))

    def addPermission(self, permission):
        self.permissions.append(permission)

    def deletePermission(self, permission):
        if permission in self.permissions:
            self.permissions.remove(permission)
    
    def getPermissions(self):
        return self.permissions

    def addComment(self, comment):
        self.comments.append(comment)

    def deleteComment(self, comment):
        if comment in self.comments:
            self.comments.remove(comment)

    def getComments(self):
        return self.comments

class Composer():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.profile = None
        self.compositions = []
        self.reviews = [] 
    
    def __eq__(self, other):
        return self.username == other.username

    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password

    def getProfile(self):
        return self.profile

    def setProfile(self, profile):
        self.profile = profile

    def addComposition(self, composition):
        compositions.append(composition)

    def deleteComposition(self, composition):
        if delComposition in self.compositions:
            self.compositions.remove(composition)

    def getCompositions(self):
        return self.compositions

    def addReview(self, review):
        reviews.append(review)
    
    def deleteReview(self, review):
        if review in self.reviews:
            self.reviews.remove(review)
    
    def getReview(self):
        return self.reviews
