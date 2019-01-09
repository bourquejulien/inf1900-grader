from urwid import (
    connect_signal,
    disconnect_signal,
    emit_signal,
    register_signal,
    )

class Controller:

    def __init__(self):
        self.signals = {}

    def emit(self, signal, *args):
        emit_signal(self, signal, *args)

    def connect(self, signal, slot, user_args=None, weak_args=None):
        return connect_signal(self, signal, slot,
                              weak_args=weak_args, user_args=user_args)
    def disconnect(self, signal, key):
        return disconect_signal(self, signal, key)

    @classmethod
    def register(cls, signals):
        register_signal(cls, signals)
