from post.Post import Post
from post.MemoryPostRepository import MemoryAnnouncementRepository


class PostService:
    @staticmethod
    def save_announcement(post: Post):
        MemoryAnnouncementRepository.save(post)

    @staticmethod
    def find_by_id(post_id: int):
        MemoryAnnouncementRepository.get_announcement_by_id(post_id)
