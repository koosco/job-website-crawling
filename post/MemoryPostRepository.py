from PostRepository import PostRepository
from post.Post import Post
from collections import defaultdict


class MemoryAnnouncementRepository(PostRepository):
    store = defaultdict(Post)
    idx = 0

    @staticmethod
    def save(announcement: Post, **kwargs):
        MemoryAnnouncementRepository.store[MemoryAnnouncementRepository.idx] = announcement
        MemoryAnnouncementRepository.idx += 1

    @staticmethod
    def get_announcement_by_id(announcement_id: int, **kwargs):
        return MemoryAnnouncementRepository.store[announcement_id]
