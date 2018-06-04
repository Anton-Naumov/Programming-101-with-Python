import vlc
from music_crawler import MusicCrawler


class MusicPlayer:
    def __init__(self):
        self._playlist = None
        self._curr_song = None
        self._song_playing = None

    def load_playlist(self, *, path, name='', repeat=False, shuffle=False):
        crawler = MusicCrawler(path)
        self._playlist = crawler.generate_playlist(name=name,
                                                   repeat=repeat,
                                                   shuffle=shuffle)

    @property
    def is_playlist_loaded(self):
        return self._playlist is not None

    def add_song(self, path):
        self._playlist.add_song(MusicCrawler.extract_song(path))

    def remove_song(self, index):
        self._playlist.remove_song(self._playlist[index])

    def play_song(self, index=-1):
        if self._curr_song is not None and index == -1:
            self._curr_song.set_pause(do_pause=0)
        elif index != -1:
            if self._curr_song is not None and self._curr_song.is_playing():
                self._curr_song.stop()

            self._curr_song = vlc.MediaPlayer(self._playlist[index].path)
            self._curr_song.play()
            self._song_playing = self._playlist[index]

    def pause_song(self):
        if self._curr_song is not None and self._curr_song.is_playing():
            self._curr_song.pause()

    def stop_song(self):
        if self._curr_song is not None and self._curr_song.is_playing():
            self._curr_song.stop()
            self._curr_song = None
            self._song_playing = None

    def print_all_songs(self):
        print(self._playlist.ppring_playlist())

    def get_all_songs_list(self):
        return self._playlist.list_with_songs()

    def get_curr_song_time(self):
        if self._curr_song is not None:
            curr_time = self._curr_song.get_time() // 1000
            return f'{curr_time // 60:02}:{curr_time % 60:02}/{self._song_playing.length()}'
        return ''


def main():
    player = MusicPlayer()
    player.load_playlist(path='/home/anton/Music/G-Eazy - The Beautiful & Damned (2017) [320]')

    player.print_all_songs()

    while(True):
        print('')
        song_idx = input('Enter index of another song to play:')
        player.play_song(int(song_idx) - 1)


if __name__ == '__main__':
    main()
