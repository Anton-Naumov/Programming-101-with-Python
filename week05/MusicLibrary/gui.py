from music_player import MusicPlayer
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.bubble import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from threading import Thread
Window.clearcolor = (.31, .31, .31, 1)
Window.size = (500, 400)


class SongsListButton(ListItemButton):
    pass


class PlayerGUI(FloatLayout):
    player = MusicPlayer()
    songs_list = ObjectProperty()
    song_time = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        directory_to_craw = input('Directory to craw for mp3 files >>>')
        self.player.load_playlist(path=directory_to_craw)
        self.songs_list.adapter.data.extend(self.player.get_all_songs_list())
        time_thread = Thread(target=self.print_curr_song_time, daemon=True)
        time_thread.start()

    def play_song(self):
        if self.songs_list.adapter.selection:
            selection = self.songs_list.adapter.data.index(self.songs_list.adapter.selection[0].text)
            self.player.play_song(selection)
            self.songs_list.adapter.selection[0].trigger_action()
        else:
            self.player.play_song()

    def pause_song(self):
        self.player.pause_song()

    def stop_song(self):
        self.player.stop_song()

    def print_curr_song_time(self):
        from time import sleep
        while True:
            sleep(0.75)
            self.song_time.text = self.player.get_curr_song_time()
            # print(f'\r{self.player.get_curr_song_time()}', end='')


class MusicPlayerApp(App):
    def build(self):
        return PlayerGUI()


if __name__ == '__main__':
    MusicPlayerApp().run()
