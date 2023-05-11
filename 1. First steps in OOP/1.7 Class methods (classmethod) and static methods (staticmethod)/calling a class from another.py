# Declare a Video class in your program with two methods:
#
# create(self, name) - to set the name name of the current video (the method stores the name name in the local
# attribute name of the Video class object);
# play(self) - to play the video (the method displays the string 'play video <name>').
#
# Declare another class named YouTube, in which declare two methods (with @classmethod decorator):
#
# add_video(cls, video) - to add a new video (the method puts the video object of the Video class into the list);
# play(cls, video_indx) - to play video from the list at the specified index (indexing from zero).
#
# (here cls is a link to the YouTube class). And the list (also inside the YouTube class):
#
# videos - to store the added objects of the Video class (initially the list is empty).
#
# The play() method of the YouTube class must access the Video class object at the index of the videos list
# and then call the play() method of the Video class.
#
# Call the add_video and play methods directly from the YouTube class.
# You do not need to create an instance of this class.
#
# Create two objects v1 and v2 of the Video class, then pass the names 'Python' and 'Python OOP' to them via
# the create() method. After that, using the add_video method of the YouTube class, add these two videos to it
# and play (using the play method of the YouTube class) first the first and then the second video.


class Video:
    def __init__(self):
        self.name = ""

    def create(self, name):
        self.name = name

    def play(self):
        print(f"play video {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()


v1 = Video()
v2 = Video()
v1.create("Python")
v2.create("Python OOP")
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)
