import pygame
import os

class Audio:
    _instance = None

    def __init__(self):
        self.__audio_folder = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../../resources/audios"
        )
        self.__sounds = self.load_sounds()
        self.__musics = self.load_musics()
        self.__volume = 0.5

    def load_sounds(self):
        sounds = {}
        for file_name in os.listdir(self.audio_folder):
            if file_name.endswith(".wav"):
                sound_path = os.path.join(self.audio_folder, file_name)
                sound_name = os.path.splitext(file_name)[0]
                sounds[sound_name] = pygame.mixer.Sound(sound_path)
        return sounds

    def load_musics(self):
        musics = {}
        for file_name in os.listdir(self.audio_folder):
            if file_name.endswith(".ogg"):
                file_path = os.path.join(self.audio_folder, file_name)
                sound_name = os.path.splitext(file_name)[0]
                musics[sound_name] = file_path
        return musics

    @property
    def audio_folder(self):
        return self.__audio_folder

    @audio_folder.setter
    def audio_folder(self, value):
        self.__audio_folder = value

    @property
    def sounds(self):
        return self.__sounds

    @sounds.setter
    def sounds(self, value):
        self.__sounds = value

    @property
    def musics(self):
        return self.__musics

    @musics.setter
    def musics(self, value):
        self.__musics = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def play_sound(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].set_volume(self.volume)
            self.sounds[sound_name].play()

    def play_music(self, music_name):
        if music_name in self.musics:
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.load(self.musics[music_name])
            pygame.mixer.music.play(-1)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
