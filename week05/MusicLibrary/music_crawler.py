import os
from mutagen.mp3 import MP3
from playlist import Playlist
from song import Song


class MusicCrawler:
    def __init__(self, path):
        self._path = path

    def generate_playlist(self, name, repeat=False, shuffle=False):
        playlist = Playlist(name=name, repeat=repeat, shuffle=shuffle)

        for root, dirs, files in os.walk(self._path):
            for file_name in files:
                extracted_song = self.extract_song(os.path.join(root, file_name))
                if extracted_song is not None:
                    playlist.add_song(extracted_song)

        return playlist

    @staticmethod
    def extract_song(file_name):
        if file_name.lower().endswith('.mp3'):
            file_type = MP3(file_name)

            if file_name is not None:
                song = Song(
                    title=file_type['TIT2'],
                    album=file_type['TPE1'],
                    artist=file_type['TPE2'],
                    length=f'0:{int(file_type.info.length)}'
                )
                song.path = os.path.join(file_name)
                return song

        return None


if __name__ == '__main__':
    mc = MusicCrawler('/home/anton/Music')

    playlist = mc.generate_playlist(name='first')

    from pprint import pprint
    pprint(playlist._songs)
