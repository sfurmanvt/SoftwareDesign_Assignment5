import time, sys
from pygame import mixer

mixer.init()
mixer.music.load(open("C:/Users/Sam/Downloads/80Degrees.mp3", "rb"))
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)
print ("done")