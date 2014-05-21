class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line



mirror = Song(["I'm Gonna Make A Change,",
                "For Once In My Life",
                "It's Gonna Feel Real Good,",
                "Gonna Make A Difference",
                "Gonna Make It Right . . ."])

beat_it = Song(["They Told Him Don't You Ever Come Around Here",
                "Don't Wanna See Your Face, You Better Disappear",
                "The Fire's In Their Eyes And Their Words Are Really Clear",
                "So Beat It, Just Beat It"])

mirror.sing_me_a_song()

beat_it.sing_me_a_song()




