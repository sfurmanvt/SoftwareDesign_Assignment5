"""
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

class Player():
    def __init__(self, *args, **kwargs):
        self.playPos = 0
        self.tracks = []
        self.numTracks = 0
        mixer.init()

    def __eq__(self, other):
        return (sorted(self.tracks) == sorted(other.tracks)) 

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
