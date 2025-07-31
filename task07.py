class Media:
    def play(self):
        return "Playing media"

class Song(Media):
    def play(self):
        return "Playing song: 🎶"

class Movie(Media):
    def play(self):
        return "Playing movie: 🎬"

class Podcast(Media):
    def play(self):
        return "Playing podcast: 🎙️"

media_list = [Song(), Movie(), Podcast()]
for m in media_list:
    print(m.play())