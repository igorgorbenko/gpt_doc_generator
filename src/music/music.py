class MusicInstrument:
    def __init__(self, player, num_strings, type='acoustic'):
        self.player = player
        self.num_strings = num_strings
        self.type = type

    def play_it(self, notes):
        if self.type == 'acoustic':
            print(f"{self.player} plays slowly {notes}")
        else:
            print(f"{self.player} plays fast {notes}!")


class Guitar(MusicInstrument):
    def __init__(self, player, num_strings, type='acoustic'):
        super().__init__(player, num_strings, type)

    def strum_chords(self, chords):
        print(f"The {self.type} {self.player} strums {chords} chords!")


class Bass(MusicInstrument):
    def __init__(self, player, num_strings, type='electric'):
        super().__init__(player, num_strings, type)

    def play_riff(self, riff):
        print(f"The {self.type} {self.player} plays a cool {riff} riff!")


class Drums(MusicInstrument):
    def __init__(self, player, num_strings=0, type='acoustic'):
        super().__init__(player, num_strings, type)

    def hit_drums(self, drum_type):
        print(f"The {self.type} {self.player} hits the {drum_type} drum!")


