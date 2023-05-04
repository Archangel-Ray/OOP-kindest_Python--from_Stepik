# Declare a class named MediaPlayer with two methods:
#
# open(file) - to open a media file named file (creates a local property filename with the value of the file argument
# in the MediaPlayer class object)
# play() - to play a media file (displays the string 'Play media file name')
#
# Create two instances of this class named media1 and media2. Call the open() method from them
# with the argument 'filemedia1' for the media1 object and 'filemedia2' for the media2 object.
# Then call the play() method through the objects.
# At the same time, two lines should be displayed on the screen (without quotes):
#
# 'filemedia1 playback'
# 'filemedia2 playback'


class MediaPlayer:

    def open(self, file):
        self.filename = file

    def play(self):
        print(self.filename, ' playback')


media1 = MediaPlayer()
media1.open('filemedia1')
media1.play()
media2 = MediaPlayer()
media2.open('filemedia2')
media2.play()
