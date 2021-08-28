class Jukebox:
    def __init__(self, cd_player, cd_collection):
        pass

    def get_current_song(self):
        pass


class CDPlayer:
    def __init__(self, cd):
        self.cd = cd

    def load_cd(self, cd):
        self.cd = cd

    def play_song(self, song):
        pass


class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def add_song(self, song):
        self.songs.append(song)


class CD:
    pass


class Song:
    pass
