import unittest

from song import Song


class TestsSong(unittest.TestCase):
    def setUp(self):
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
            length="1:23:45"
        )

    def test_init_working_correctly(self):
        self.assertEqual('Odin', self.song._title)
        self.assertEqual('Manowar', self.song._artist)
        self.assertEqual('The Sons of Odin', self.song._album)
        self.assertEqual((0, 3, 44), self.song._length)

    def test_init_throws_exception_on_invalid_length(self):
        with self.assertRaises(ValueError) as e:
            Song(
                title="Odin",
                artist="Manowar",
                album="The Sons of Odin",
                length="abc"
            )

        self.assertEqual(
            'The length is invalid!',
            str(e.exception)
        )

    def test_set_length_with_minutes_and_seconds(self):
        self.song.set_length('13:33')

        self.assertEqual(self.song._length, (0, 13, 33))

    def test_set_length_with_hours_minutes_and_seconds(self):
        self.song.set_length('1:45:54')

        self.assertEqual(self.song._length, (1, 45, 54))

    def test_set_length_raises_exception_on_invalid_length(self):
        with self.subTest('With random string'):
            with self.assertRaises(ValueError) as e:
                self.song.set_length('abc')

            self.assertEqual(
                'The length is invalid!',
                str(e.exception)
            )

        with self.subTest('With only seconds'):
            with self.assertRaises(ValueError) as e:
                self.song.set_length('45')

            self.assertEqual(
                'The length is invalid!',
                str(e.exception)
            )

    def test_get_raw_length(self):
        self.assertEqual((0, 3, 44), self.song.get_raw_length())

    def test_length_raises_exception_with_more_than_one_argument(self):
        with self.subTest('With two arguments'):
            with self.assertRaises(Exception) as e:
                self.song.length(seconds=True, minutes=True)

            self.assertEqual(
                'Invalid arguments!',
                str(e.exception)
            )

        with self.subTest('With three arguments'):
            with self.assertRaises(Exception) as e:
                self.song.length(seconds=True, minutes=True, hours=True)

            self.assertEqual(
                'Invalid arguments!',
                str(e.exception)
            )

    def test_length_with_no_arguments(self):
        with self.subTest('When the length has only minutes and seconds'):
            self.assertEqual(
                '03:44',
                self.song.length()
            )

        with self.subTest('When the length has hours, minutes and seconds'):
            self.assertEqual(
                '1:23:45',
                self.song1.length()
            )

    def test_length_with_seconds_argument(self):
        self.assertEqual(5025, self.song1.length(seconds=True))

    def test_length_with_minutes_argument(self):
        self.assertEqual(83, self.song1.length(minutes=True))

    def test_length_with_hours_argument(self):
        self.assertEqual(1, self.song1.length(hours=True))

    def test_str_working_correctly(self):
        self.assertEqual(
            'artist - title from album - 1:23:45',
            str(self.song1)
        )

    def test_eq_returning_False(self):
        with self.subTest('With difference in every argument'):
            self.assertFalse(self.song == self.song1)

        with self.subTest('With difference in three of the arguments'):
            self.assertFalse(self.song == Song(
                                                title="title",
                                                artist="artist",
                                                album="album",
                                                length="3:14"
                                            ))

            self.assertFalse(self.song == Song(
                                                title="title",
                                                artist="artist",
                                                album="The Sons of Odin",
                                                length="0:00"
                                            ))

        with self.subTest('With difference in two of the arguments'):
            self.assertFalse(self.song == Song(
                                                title="Odin",
                                                artist="Manowar",
                                                album="album",
                                                length="0:00"
                                            ))

            self.assertFalse(self.song == Song(
                                                title="Odin",
                                                artist="artist",
                                                album="The Sons of Odin",
                                                length="0:00"
                                            ))

        with self.subTest('With difference in one of the arguments'):
            self.assertFalse(self.song == Song(
                                                title="Odin",
                                                artist="Manowar",
                                                album="The Sons of Odin",
                                                length="0:00"
                                            ))

            self.assertFalse(self.song == Song(
                                                title="title",
                                                artist="Manowar",
                                                album="The Sons of Odin",
                                                length="3:44"
                                            ))

    def test_eq_returning_true(self):
        self.assertTrue(self.song == Song(
                                            title="Odin",
                                            artist="Manowar",
                                            album="The Sons of Odin",
                                            length="3:44"
                                        ))

    def test_hash_working_correctly(self):
        self.assertEqual(hash(self.song), hash(str(self.song)))

    def test_as_json_dict(self):
        expected = ({
                        "title": "Odin",
                        "artist": "Manowar",
                        "album": "The Sons of Odin",
                        "length": "03:44"
                    })

        self.assertDictEqual(self.song.as_json_dict(), expected)

    def test_from_json(self):
        json_dict = {
                    "title": "Odin",
                    "artist": "Manowar",
                    "album": "The Sons of Odin",
                    "length": "03:44"
                    }

        self.assertEqual(self.song, Song.from_json(json_dict))


if __name__ == '__main__':
    unittest.main()
