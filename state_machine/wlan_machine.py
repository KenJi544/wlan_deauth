from .wlan_states import Monitor_disabled


class Wlan(Monitor_disabled):

    def __init__(self):
        self.state = Monitor_disabled()

    def on_event(self, event):
        self.state = self.state.on_event(event)
    
