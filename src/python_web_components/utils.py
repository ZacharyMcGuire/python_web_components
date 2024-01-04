class Observable:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer()


class State(Observable):
    def __init__(self, initial_state=None):
        super().__init__()
        self._state = initial_state or {}

    def __getitem__(self, key):
        return self._state[key]

    def __setitem__(self, key, value):
        self._state[key] = value
        self.notify()
