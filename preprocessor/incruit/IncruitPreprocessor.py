from domain.post.Post import Post
from collections import deque
from datetime import datetime, timedelta
from copy import deepcopy
import re

from ParamPrinter import ParamPrinter


class IncruitPreprocessor:
    def __init__(self, post: Post):
        self.posts = deque()
        self.posts.append(post)

    def career(self):
        for i in range(len(self.posts)):
            post = self.posts.popleft()

            post.career = post.career.replace('이상', '')
            post.career = post.career.replace('↑', '')
            careers = post.career.split('/')
            new_post = deepcopy(post)
            for career in careers:
                new_post.career = career
                self.posts.append(new_post)  # 신입/경력 -> ['신입', '경력']

    def education(self):
        for i in range(len(self.posts)):
            post = self.posts.popleft()
            post.education = post.education.replace('이상', '').strip()  # 대졸 이상 -> 대졸
            post.education = post.education.replace('↑', '').strip()  # 대졸↑ -> 대졸
            post.education = post.education.replace('학력', '').strip()  # 학력무관 -> 무관
            self.posts.append(post)

    def deadline(self):
        for i in range(len(self.posts)):
            post = self.posts.popleft()
            if post.deadline in ('상시', '채용시'):
                # 상시 또는 채용시 공고
                post.deadline = None
            elif post.deadline.startswith('~'):
                # ~02.04
                post.deadline = post.deadline[1:6].replace('.', '-')
                current_year = datetime.now().year
                date = f'{current_year}-{post.deadline}'
                formatted_date = datetime.strptime(date, '%Y-%m-%d')
                post.deadline = formatted_date.date()

    def created_at(self):
        for i in range(len(self.posts)):
            post = self.posts.popleft()
            create_time = datetime.now().date()
            if '시간' in post.created_at:
                # n시간 전 공고
                post.created_at = create_time
            elif '일전' in post.created_at:
                # n일 전 공고
                posted_date = re.findall(r'\d+', post.created_at)
                print(type(create_time))
                post.created_at = create_time - timedelta(days=int(posted_date[0]))
            self.posts.append(post)

    def process(self):
        self.career()
        self.education()
        self.deadline()
        self.created_at()
        items = []
        for post in self.posts:
            items.append(post)
        return items


if __name__ == '__main__':
    from domain.post.PostBuilder import PostBuilder
    from ParamPrinter import ParamPrinter

    builder = PostBuilder()
    item = (builder.company_name("충북개발공사").
            post_name("2024년 정규직(신입/경력) 채용 공고").
            career("신입/경력(연차무관)").
            education("박사 이상").
            location("충북 청주시").
            job_type("정규직").
            deadline("~02.08 (목)").
            url("https://job.incruit.com/jobdb_info/jobpost.asp?job=2401290004100").
            created_at("(3일전 등록)").build())
    ParamPrinter.print_class_params(item)
    preprocessor = IncruitPreprocessor(item)
    preprocessor.process()
