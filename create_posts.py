import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from faker import Faker
from boards.models import Master, Post
from django.contrib.auth.models import User

fake = Faker('ko_KR')

# 'notice' slug의 Master 가져오기 또는 생성
master, created = Master.objects.get_or_create(slug='notice', defaults={'name': 'Notice Board', 'description': '공지사항 게시판'})

# User가 있어야 해요. 첫 번째 User를 가져오거나 생성
user = User.objects.first()
if not user:
    user = User.objects.create_user(username='testuser', password='password')

# 300개 Post 생성
for _ in range(300):
    Post.objects.create(
        master=master,
        title=fake.sentence(nb_words=5),
        content=fake.text(max_nb_chars=500),
        author=user
    )

print("300개의 랜덤 게시물이 생성되었습니다.")