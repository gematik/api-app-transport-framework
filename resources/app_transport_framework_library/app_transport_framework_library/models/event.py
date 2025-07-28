class Event:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, callback):
        self._subscribers.append(callback)

    def unsubscribe(self, callback):
        self._subscribers.remove(callback)

    def trigger(self, *args, **kwargs):
        for callback in self._subscribers:
            callback(*args, **kwargs)
