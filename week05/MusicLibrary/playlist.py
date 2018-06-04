import json
from song import Song
from random import randint
from utility import format_length


class Playlist:
    def __init__(self, *, name, repeat=False, shuffle=False):
        self._name = name
        self._repeat = repeat
        self._shuffle = shuffle
        self._songs = []
        self._not_played_songs_idxs = []

    def add_song(self, song):
        if song in self._songs:
            raise ValueError('The song is already in the playlist!')

        self._songs.append(song)
        self._not_played_songs_idxs.append(len(self._songs) - 1)

    def remove_song(self, song):
        try:
            idx_to_delete = self._songs.index(song)
            self._songs.remove(song)
        except ValueError:
            raise ValueError('The song is not in the playlist!')

        if idx_to_delete in self._not_played_songs_idxs:
            self._not_played_songs_idxs.remove(idx_to_delete)

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def total_length(self):
        length = [0, 0, 0]

        for song in self._songs:
            for pos, el in enumerate(song.get_raw_length()):
                length[pos] += el

        hours, minutes, seconds = format_length(length[0], length[1], length[2])

        return f'{hours}:{minutes:02}:{seconds:02}'

    def artists(self):
        histogram = {}

        for song in self._songs:
            histogram[song.artist] = histogram.get(song.artist, 0) + 1

        return histogram

    def next_song(self):
        if len(self._songs) is 0 or\
           (len(self._not_played_songs_idxs) is 0 and self._repeat is False):
            return None

        if len(self._not_played_songs_idxs) is 0:
            self._not_played_songs_idxs = list(range(0, len(self._songs)))

        idx_of_next_song = self._not_played_songs_idxs[0]
        l = len(self._not_played_songs_idxs)
        if self._shuffle is True:
            idx_of_next_song = self._not_played_songs_idxs[randint(0, l - 1)]

        self._not_played_songs_idxs.remove(idx_of_next_song)
        return self._songs[idx_of_next_song]

    def __getitem__(self, index):
        if index < 0 or index >= len(self._songs):
            raise IndexError('Invalid song index!')

        return self._songs[index]

    def ppring_playlist(self):
        from tabulate import tabulate

        headers = ['', 'Artist', 'Song', 'Lenght']
        information = []

        for idx, song in enumerate(self._songs):
            information.append([str(idx + 1), song.artist, song.title, song.length()])

        if information == []:
            return 'The playlist is empty.'

        return tabulate(information, headers=headers, tablefmt='orgtbl')

    def as_json_dict(self):
        return {
            "name": self._name,
            "repeat": self._repeat,
            "shuffle": self._shuffle,
            "songs": [song.as_json_dict() for song in self._songs]
        }

    @classmethod
    def from_json(cls, json_dict):
        playlist = cls(
            name=json_dict["name"],
            repeat=json_dict["repeat"],
            shuffle=json_dict["shuffle"]
        )

        for song_as_json in json_dict["songs"]:
            playlist.add_song(Song.from_json(song_as_json))

        return playlist

    def save(self):
        name = self._name.replace(' ', '-')
        file_name = f'{name}.json'

        with open(file_name, 'w') as out_file:
            json.dump(self.as_json_dict(), out_file)

    @classmethod
    def load(cls, file_name):
        with open(file_name, 'r') as in_file:
            data = json.load(in_file)
        return Playlist.from_json(data)

    # not tested
    def list_with_songs(self):
        information = []

        for idx, song in enumerate(self._songs):
            information.append(f'{str(idx + 1)}. {song.artist}, {song.title}, {song.length()}')

        return information
