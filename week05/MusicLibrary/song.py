from utility import format_length


class Song:
    def __init__(self, *, title, artist, album, length):
        self._title = title
        self._artist = artist
        self._album = album
        self.set_length(length)

    def set_length(self, length):
        parts = length.split(':')

        if (len(parts) is not 2 and len(parts) is not 3) or\
           sum([part.isdigit() for part in parts]) != len(parts):
            raise ValueError('The length is invalid!')

        if len(parts) == 2:
            self._length = format_length(0, int(parts[0]), int(parts[1]))
            return

        self._length = format_length(int(parts[0]), int(parts[1]), int(parts[2]))

    def get_raw_length(self):
        return self._length

    def length(self, seconds=False, minutes=False, hours=False):
        if sum(arg is True for arg in [seconds, minutes, hours]) > 1:
            raise Exception('Invalid arguments!')

        if seconds is True:
            return self._length[0]*3600 + self._length[1]*60 + self._length[2]

        if minutes is True:
            return self._length[0]*60 + self._length[1]

        if hours is True:
            return self._length[0]

        if self._length[0] is 0:
            return f'{self._length[1]:02}:{self._length[2]:02}'

        return f'{self._length[0]}:{self._length[1]:02}:{self._length[2]:02}'

    def __str__(self):
        return f'{self._artist} - {self._title} '\
               f'from {self._album} - {self.length()}'

    @property
    def artist(self):
        return self._artist

    @property
    def title(self):
        return self._title

    @property
    def album(self):
        return self._album

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (
            self._title == other._title and
            self._artist == other._artist and
            self._album == other._album and
            self._length == other._length
        )

    def __hash__(self):
        return hash(str(self))

    def as_json_dict(self):
        return {
            "title": self._title,
            "artist": self._artist,
            "album": self._album,
            "length": self.length()
        }

    @classmethod
    def from_json(cls, json_dict):
        return cls(
            title=json_dict["title"],
            artist=json_dict["artist"],
            album=json_dict["album"],
            length=json_dict["length"]
        )
