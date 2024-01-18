from abc import ABC, abstractmethod
from ..domain.Announcement import Announcement

class AnnouncementRepository(ABC):
    @abstractmethod
    def save(self, announcement: Announcement):
        pass

    @abstractmethod
    def get_announcement_by_id(self, announcement_id: int):
        pass
