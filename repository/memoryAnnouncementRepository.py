from AnnouncementRepository import AnnouncementRepository
from domain.Announcement import Announcement
from collections import defaultdict


class MemoryAnnouncementRepository(AnnouncementRepository):
    store = defaultdict(Announcement)

    @staticmethod
    def save(announcement: Announcement, **kwargs):
        idx = announcement.idx
        MemoryAnnouncementRepository.store[idx] = announcement

    @staticmethod
    def get_announcement_by_id(announcement_id: int, **kwargs):
        return MemoryAnnouncementRepository.store[announcement_id]
