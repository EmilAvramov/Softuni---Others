class Music:
    def __init__(self, _title: str, _artist: str, _lyrics: str) -> None:
        self.title = _title
        self.artist = _artist
        self.lyrics = _lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
