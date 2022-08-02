class Self:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age


    def get_d_mame(self):
        print(f" Hello, my name is {self.name} {self.lastname}, and I’m {self.age} years old")

about_self = Self("Carl", "Johnson ", "26")
about_self.get_d_mame()



class Dog:
    def __init__(self, age_dog):
        self.age_dog = age_dog


    def age_human(self):
        fact_ = self.age_dog * 7
        print(fact_)
        return fact_

about_age = Dog(2)
about_age.age_human()


CHANNELS = ["BBC", "Discovery", "TV1000"]
chan_ = CHANNELS

class TVController:
    def __init__(self, channels):
        self._channels = channels
        self._current_channel = 0

    def first_channel(self):
        return self.turn_channel(1)

    def last_channel(self):

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

    def is_exist(BBC):

        if BBC in chan_:
            return 'Yes'
        else:
            return 'No'


    def is_exist(N):
        if N <= len(chan_) and N > 0:
            return 'Yes'
        else:
            return 'No'
