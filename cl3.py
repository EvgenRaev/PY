CHANNELS = ["BBC", "Discovery", "TV1000"]


class VoiceCommand:
    def __init__(self, channels):
        self._channels = channels
        self._current_channel = 0

    def first_channel(self):
        return self.turn_channel(1)

    def last_channel(self):
        print(self.turn_channel(len(self._channels)))
        return self.turn_channel(len(self._channels))

    def turn_channel(self, channel_number):
        self._current_channel = channel_number - 1

        return self.current_channel()

    def _previous_next(self, delta):
        self._current_channel = (self._current_channel + delta) % len(self._channels)
        return self.current_channel()

    def next_channel(self):
        return self._previous_next(1)

    def previous_channel(self):
        return self._previous_next(-1)

    def current_channel(self):
        return self._channels[self._current_channel]

    def is_exist(self, x):
        x = list ("BBC", "Discovery", "TV1000")
        for a in x:
            if a in x and len(x) <= a:
                return ("Yes")
            else:
                return ("No")


controller = VoiceCommand(CHANNELS)

controller.last_channel()
controller.is_exist(5)