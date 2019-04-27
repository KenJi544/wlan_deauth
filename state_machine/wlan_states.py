from .state import State


class Monitor_enabled(State):
    """
    The state that indicates that the wlan is in monitor mod
    """

    def on_event(self, event):
        if event == 'disable':
            return Monitor_disabled()

        return self


class Monitor_disabled(State):
    """
    The state that indicates that the wlan is not in monitor mod
    """

    def on_event(self, event):
        if event == 'enable':
            return Monitor_enabled()

        return self

