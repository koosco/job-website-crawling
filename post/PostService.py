from domain.post.Post import Post
from repository.post.MemoryPostRepository import MemoryPostRepository


class PostService:
    @staticmethod
    def save_announcement(post: Post):
        MemoryPostRepository.save(post)

    @staticmethod
    def find_by_id(post_id: int):
        MemoryPostRepository.get_announcement_by_id(post_id)
