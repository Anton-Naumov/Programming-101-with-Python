import unittest

from song import Song
from playlist import Playlist


class TestsPlaylist(unittest.TestCase):
    def setUp(self):
        self.playlist_both = Playlist(name="Code", repeat=True, shuffle=True)
        self.playlist_shuffle = Playlist(name="Code", shuffle=True)
        self.playlist_repeat = Playlist(name='Code', repeat=True)
        self.playlist_none = Playlist(name='Code')

        self.song = Song(
            title="Odin",
            artist="Manowar",
            album="The Sons of Odin",
            length="3:44"
        )

        self.song1 = Song(
            title="title",
            artist="artist",
            album="album",
            length="1:58:45"
        )

        self.new_song1 = Song(title='Him & I', artist='G-eazy', album='', length='4:28')
        self.new_song2 = Song(title='Eazy', artist='G-eazy', album='', length='5:09')

        self.playlist = Playlist(name="Code", repeat=True)
        self.playlist._songs = [self.song, self.song1, self.new_song1, self.new_song2]
        self.playlist._not_played_songs_idxs = [0, 1]

    def test_init_(self):
        with self.subTest('With name, repeat and shuffle arguments'):
            self.assertEqual(self.playlist_both._name, 'Code')
            self.assertTrue(self.playlist_both._repeat)
            self.assertTrue(self.playlist_both._shuffle)
            self.assertEqual(self.playlist_both._songs, [])
            self.assertEqual(self.playlist_both._not_played_songs_idxs, [])

        with self.subTest('With name and shuffle arguments'):
            self.assertEqual(self.playlist_shuffle._name, 'Code')
            self.assertFalse(self.playlist_shuffle._repeat)
            self.assertTrue(self.playlist_shuffle._shuffle)
            self.assertEqual(self.playlist_shuffle._songs, [])
            self.assertEqual(self.playlist_shuffle._not_played_songs_idxs, [])

        with self.subTest('With name and repeat arguments'):
            self.assertEqual(self.playlist_repeat._name, 'Code')
            self.assertTrue(self.playlist_repeat._repeat)
            self.assertFalse(self.playlist_repeat._shuffle)
            self.assertEqual(self.playlist_repeat._songs, [])
            self.assertEqual(self.playlist_repeat._not_played_songs_idxs, [])

        with self.subTest('With only name argument'):
            self.assertEqual(self.playlist_none._name, 'Code')
            self.assertFalse(self.playlist_none._repeat)
            self.assertFalse(self.playlist_none._shuffle)
            self.assertEqual(self.playlist_none._songs, [])
            self.assertEqual(self.playlist_none._not_played_songs_idxs, [])

    def test_add_song_when_shuffle_argument_is_False(self):
        self.playlist_repeat.add_song(self.song)

        self.assertEqual(self.playlist_repeat._songs, [self.song])
        self.assertEqual(self.playlist_repeat._not_played_songs_idxs, [0])

    def test_add_song_raises_exception_when_the_song_is_already_in_the_playlist(self):
        with self.assertRaises(ValueError) as e:
            self.playlist.add_song(self.song)

        self.assertEqual(
            'The song is already in the playlist!',
            str(e.exception)
        )

    def test_remove_song_raises_exception(self):
        with self.subTest('When song is not in the songs list or songs_playes list'):
            with self.assertRaises(ValueError) as e:
                self.playlist_repeat.remove_song(self.song)

            self.assertEqual(
                'The song is not in the playlist!',
                str(e.exception)
            )

    def test_remove_song_removes_song_from_songs_list_if_song_was_not_yet_played(self):
        self.playlist.remove_song(self.song)

        self.assertEqual(self.playlist._songs, [self.song1,
                                                self.new_song1,
                                                self.new_song2])
        self.assertEqual(self.playlist._not_played_songs_idxs, [1])

    def test_remove_song_removes_song_from_songs_list_if_song_was_already_played(self):
        self.playlist.remove_song(self.new_song1)

        self.assertEqual(self.playlist._songs, [self.song,
                                                self.song1,
                                                self.new_song2])
        self.assertEqual(self.playlist._not_played_songs_idxs, [0, 1])

    def test_add_songs_working_correctly(self):
        self.playlist_repeat.add_songs([self.new_song1, self.new_song2])

        self.assertEqual(
            self.playlist_repeat._songs,
            [self.new_song1, self.new_song2]
        )

        self.assertEqual(
            self.playlist._not_played_songs_idxs,
            [0, 1]
        )

    def test_total_length_with_no_songs_in_the_playlist(self):
        self.assertEqual(self.playlist_shuffle.total_length(), '0:00:00')

    def test_total_length_with_more_than_60_seconds_total(self):
        self.playlist._songs = [self.song, self.new_song1]

        self.assertEqual(self.playlist.total_length(), '0:08:12')

    def test_total_length_with_more_than_60_minutes_total(self):
        self.playlist._songs = [self.song1, self.new_song2]

        self.assertEqual(self.playlist.total_length(), '2:03:54')

    def test_artists_with_no_songs(self):
        self.assertDictEqual(self.playlist_both.artists(), {})

    def test_artists_with_songs(self):
        self.assertDictEqual(self.playlist.artists(), {
                                                        'Manowar': 1,
                                                        'artist': 1,
                                                        'G-eazy': 2
                                                      })

    def test_next_song_returns_None_when_there_are_no_songs(self):
            self.assertEqual(self.playlist_shuffle.next_song(), None)

    def test_next_song_returns_None_when_no_songs_left_to_play_and_repeat_is_False(self):
            self.assertEqual(self.playlist_shuffle.next_song(), None)

    def test_next_song_if_there_are_songs_left_to_play_and_shuffle_is_False(self):
        song = self.playlist.next_song()

        self.assertEqual(song, self.song)
        self.assertEqual(self.playlist._not_played_songs_idxs, [1])

    def test_next_song_if_there_are_no_songs_left_to_play_and_repeat_is_True(self):
        self.playlist._not_played_songs_idxs = []

        song = self.playlist.next_song()

        self.assertEqual(song, self.song)
        self.assertEqual(self.playlist._not_played_songs_idxs, [1, 2, 3])

    def test_getitem_raises_exception_on_invalid_index(self):
        with self.assertRaises(IndexError) as e:
            self.playlist[5]

        self.assertEqual(
            str(e.exception),
            'Invalid song index!'
        )

    def test_getitem_song_on_invalid_index(self):
        self.assertEqual(self.playlist[2], self.new_song1)

    def test_pprit_playlist_with_songs(self):
        expected = ('|    | Artist   | Song    | Lenght   |\n'
                    '|----+----------+---------+----------|\n'
                    '|  1 | Manowar  | Odin    | 03:44    |\n'
                    '|  2 | artist   | title   | 1:58:45  |\n'
                    '|  3 | G-eazy   | Him & I | 04:28    |\n'
                    '|  4 | G-eazy   | Eazy    | 05:09    |')

        self.assertEqual(self.playlist.ppring_playlist(), expected)

    def test_as_json_dict(self):
        playlist = Playlist(name='Code', repeat=True)
        playlist._songs = [self.song, self.new_song1]

        expected = {
            'name': 'Code',
            'repeat': True,
            'shuffle': False,
            'songs': [
                {
                    'title': 'Odin',
                    'artist': 'Manowar',
                    'album': 'The Sons of Odin',
                    'length': '03:44'
                }, {
                    'title': 'Him & I',
                    'artist': 'G-eazy',
                    'album': '',
                    'length': '04:28'}
                ]
        }

        self.assertEqual(playlist.as_json_dict(), expected)

    def test_from_json(self):
        json_dict = {
            'name': 'Code',
            'repeat': True,
            'shuffle': False,
            'songs': [
                {
                    'title': 'Odin',
                    'artist': 'Manowar',
                    'album': 'The Sons of Odin',
                    'length': '03:44'
                }, {
                    'title': 'Him & I',
                    'artist': 'G-eazy',
                    'album': '',
                    'length': '04:28'}
                ]
        }

        playlist = Playlist.from_json(json_dict)

        self.assertEqual(playlist._name, 'Code')
        self.assertTrue(playlist._repeat)
        self.assertFalse(playlist._shuffle)
        self.assertEqual(playlist._songs, [self.song, self.new_song1])

    def test_json_serializing_and_deserializing(self):
        playlist1 = Playlist(name='Code', repeat=True)
        playlist1._songs = [self.song, self.new_song1]

        playlist1.save()

        playlist = Playlist.load('Code.json')

        self.assertEqual(playlist._name, 'Code')
        self.assertTrue(playlist._repeat)
        self.assertFalse(playlist._shuffle)
        self.assertEqual(playlist._songs, [self.song, self.new_song1])


if __name__ == '__main__':
    unittest.main()
