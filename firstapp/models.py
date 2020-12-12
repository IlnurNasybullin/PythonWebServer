from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


def get_posts(search_query):
    posts = Post.objects.all()
    if search_query:
        posts = posts.filter(title__icontains=search_query)
    return posts


class Student(models.Model):
    group = models.CharField('Группа', max_length=10)
    name = models.CharField('Имя', max_length=50)
    lastname = models.CharField('Фамилия',max_length=50)
    age = models.IntegerField('Возраст')
    hobbies = models.TextField('Интересы')

    def __str__(self):
        return self.group


def get_students(search_query):
    students = Student.objects.all()
    if search_query:
        students = students.filter(lastname__icontains=search_query)
    return students