class Guitar:

    def play(self):
        return 'Playing the guitar'


def start_playing(obj):
    return obj.play()

guitar = Guitar()

print(playing(guitar))