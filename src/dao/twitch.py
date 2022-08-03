from twitchAPI.twitch import Twitch


class Twitch:
    def __init__(self, app_id, secret_key):
        self._twitch = Twitch(app_id, secret_key)

    @property
    def twitch(self):
        return self._twitch
