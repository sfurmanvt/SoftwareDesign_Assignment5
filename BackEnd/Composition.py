"""
AUTHOR: Virginia Tech Lacrosse Team

Functionality for storing and manipulating compositions

DIFFERENCES FROM CLASS DIAGRAM:

__eq__ methods added across each of the classes to allow for comparison
Overloaded Constructors accomplished through python's kwargs system
(you can pass in a variable number of keyworded arguments)

Note:
    startingTime renamed to starting Beat For Clarity
    Added ability to translate frequency into its corresponding note letter
Compostion:
    Added member variable to track bpm and corresponding getters and setters


"""
from scipy.io.wavfile import read
import numpy as np

class Instrument():
    def __init__(self, name, audioFile):
        self.name = name
        self.audio = np.array(read(audioFile)[1],dtype=float)

    def __eq__(self, other):
        return (self.name == other.name)
    
    def getSound(self):
        return self.audio

class Note():
    def __init__(self, *args, **kwargs):
        self.instrument = kwargs.get('instrument', None)
        self.frequency = kwargs.get('frequency', None)
        self.duration = kwargs.get('duration', None)
        self.startingBeat = kwargs.get('startingBeat', None)
        self.FrequencyToLetter= {
            16 : ('C', 0),
            18 : ('D', 0),
            21 : ('E', 0),
            22 : ('F', 0),
            25 : ('G', 0),
            28 : ('A', 1),
            31 : ('B', 1),
            33 : ('C', 1),
            37 : ('D', 1),
            41 : ('E', 1),
            44 : ('F', 1),
            49 : ('G', 1),
            55 : ('A', 2),
            62 : ('B', 2),
            65 : ('C', 2),
            73 : ('D', 2),
            82 : ('E', 2),
            87 : ('F', 2),
            98 : ('G', 2),
            110 : ('A', 3),
            123 : ('B', 3),
            131 : ('C', 3),
            147 : ('D', 3),
            165 : ('E', 3),
            175 : ('F', 3),
            196 : ('G', 3),
            220 : ('A', 4),
            247 : ('B', 4),
            262 : ('C', 4),
            294 : ('D', 4),
            330 : ('E', 4),
            349 : ('F', 4),
            392 : ('G', 4),
            440 : ('A', 5),
            494 : ('B', 5),
            523 : ('C', 5),
            587 : ('D', 5),
            659 : ('E', 5),
            698 : ('F', 5),
            784 : ('G', 5),
            880 : ('A', 6),
            988 : ('B', 6),
            1047 : ('C', 6),
            1175 : ('D', 6),
            1319 : ('E', 6),
            1397 : ('F', 6),
            1568 : ('G', 6),
            1760 : ('A', 7),
            1976 : ('B', 7),
            2093 : ('C', 7),
            2349 : ('D', 7),
            2637 : ('E', 7),
            2794 : ('F', 7),
            3136 : ('G', 7),
            3520 : ('A', 8),
            3951 : ('B', 8),
            4186 : ('C', 8),
            4699 : ('D', 8),
            5274 : ('E', 8),
            5588 : ('F', 8),
            6272 : ('G', 8)
        }

    def __eq__(self, other):
        return(self.instrument == other.instrument
        and self.duration == other.duration
        and self.frequency == other.frequency
        and self.startingBeat == other.startingBeat)

    def getInstrument(self):
        return self.instrument

    def setInstrument(self, instrument):
        self.instrument = instrument

    def getFrequency(self):
        return self.frequency

    def setFrequency(self, frequency):
        self.frequency = frequency

    def getStartingBeat(self):
        return self.startingBeat

    def setStartingBeat(self, startingBeat):
        self.startingBeat = startingBeat

    def getDuration(self):
        return self.duration

    def setDuration(self, duration):
        self.duration = duration

    def getNoteLetter(self):
        return self.FrequencyToLetter.get(self.frequency, None)

class Measure():
    def __init__(self, *args, **kwargs):
        self.keySignature = kwargs.get('keysignature', None)
        self.timeSignature = kwargs.get('timesignature', None)
        self.notes = []
        self.notesDuration = 0

    def __eq__(self, other):
        return (self.keySignature == other.keySignature
        and self.timeSignature == other.timeSignature
        and self.notes == other.notes
        and self.notesDuration == other.notesDuration)

    def getKeySignature(self):
        return self.keySignature

    def setKeySignature(self, keySignature):
        self.keySignature = keySignature

    def getTimeSignature(self):
        return self.timeSignature

    def setTimeSignature(self, timeSignature):
        self.timeSignature = timeSignature

    def addNote(self, note):
        if note.getDuration() + self.notesDuration <= self.timeSignature:
            self.notes.append(note)
            self.notesDuration += note.getDuration()

    def removeNote(self, note):
        if note in self.notes:
            self.notes.remove(note)
            self.notesDuration -= note.getDuration()
    

class Composition():
    def __init__(self, *args, **kwargs):
        self.measures = []
        self.reviews = []
        self.bpm = 0
        self.description = kwargs.get('description', '')

    def __eq__(self, other):
        return (self.measures == other.measures
        and sorted(self.reviews) == sorted(other.reviews)
        and self.description == other.description)

    def addMeasure(self, measure):
        self.measures.append(measure)

    def deleteMesure(self, measure):
        if measure in self.measures:
            self.measures.remove(measure)

    def addReview(self, review):
        self.reviews.append(review)

    def deleteReview(self, review):
        if review in self.reviews:
            self.reviews.remove(review)

    def getMeasures(self):
        return self.measures
    
    def getReviews(self):
        return self.reviews

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description
    
    def getBPM(self):
        return self.bpm

    def setBPM(self, bpm):
        self.bpm = bpm