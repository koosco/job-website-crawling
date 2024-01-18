from ..domain.Announcement import Announcement
from ..repository.memoryAnnouncementRepository import MemoryAnnouncementRepository


class AnnouncementService:
    @staticmethod
    def save_announcement(announcement: Announcement):
        MemoryAnnouncementRepository.save(announcement)

    @staticmethod
    def find_by_id(announcement_id: int):
        MemoryAnnouncementRepository.get_announcement_by_id(announcement_id)
