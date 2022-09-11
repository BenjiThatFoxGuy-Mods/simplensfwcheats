from sims4communitylib.events.event_handling.common_event_registry import CommonEventRegistry
from sims4communitylib.events.zone_spin.events.zone_late_load import S4CLZoneLateLoadEvent
from sims4communitylib.notifications.common_basic_notification import CommonBasicNotification


class S4CLSampleModShowLoadedMessage:
    """ A class that listens for a zone load event and shows a notification upon loading into a household. """
    @staticmethod
    def show_loaded_notification() -> None:
        """ Show that the mod has loaded. """
        notification = CommonBasicNotification(
            'Simple NSFW Cheats by BenjiThatFoxGuy v0.1',
            'all seems to be working in order! this mod relies on the cheats menu. to learn more, type simplensfwcheatshelp into the cheat console. all is subject to change in the future!'
        )
        notification.show()

    @staticmethod
    @CommonEventRegistry.handle_events('benjithatfoxguy_simplensfwcheats')
    def _show_loaded_notification_when_loaded(event_data: S4CLZoneLateLoadEvent):
        if event_data.game_loaded:
            # If the game has not loaded yet, we don't want to show our notification.
            return
        S4CLSampleModShowLoadedMessage.show_loaded_notification()
