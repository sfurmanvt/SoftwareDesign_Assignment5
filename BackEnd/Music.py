"""
AUTHOR: Virginia Tech Lacrosse Team

Functionality for storing and manipulating compositions

DIFFERENCES FROM CLASS DIAGRAM:
This class is new, due to a switch to using JS for the front end instead of a
locally running client. This is a small class which handles the loading and
actual playing of music in the collaborative editor. It allows tracks to be
strung together and played on a player. The closest thing to this in the original
design would be the ClientLogic class, which originally had methods for
playing compositions, but would not work in a form we could implement fast
enough for the scope of this class. Thus, we did this instead.
"""

from pygame import mixer

class Track():
    def __init__(self, musicFile, *args, **kwargs):
        self.title = kwargs.get('title', '')
        self.artist = kwargs.get('artist', '')
        self.genre = kwargs.get('genre', '')
        self.file = open(musicFile, 'rb')

    def __str__(self):
        return '{0:s} by {1:s}'.format(self.title, self.artist)

    def getFile(self):
        return self.file

    def getTitle(self):
        return self.title
    
    def getArtist(self):
        return self.artist
    
    def getGenre(self):
        return self.genre

class Player():
    def __init__(self, *args, **kwargs):
        self.playPos = 0
        self.tracks = []
        self.numTracks = 0
        mixer.init()

    def addTrack(self, track):
        self.tracks.append(track)
        self.numTracks += 1
        
    def addTracks(self, trackList):
        for track in trackList:
            self.addTrack(track)

    def playTrack(self):
        mixer.music.play()

    def pauseTrack(self):
        mixer.music.pause()

    def unpauseTrack(self):
        mixer.music.unpause()

    def stopTrack(self):
        mixer.music.stop()

    def loadNextTrack(self):
        if self.playPos < self.numTracks:
            mixer.music.load(self.tracks[self.playPos].getFile())
            self.playPos += 1

    def loadPrevTrack(self):
        if self.playPos > 0:
            mixer.music.load(self.tracks[self.playPos - 1].getFile())
            self.playPos -= 1

    def isPlaying(self):
        return mixer.get_busy()
