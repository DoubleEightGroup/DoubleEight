from django.db import models

# Create your models here.
class Userinfo(models.Model):
    username=models.CharField(max_length=32,unique=True)
    nickname=models.CharField(max_length=32,unique=True)
    password=models.CharField(max_length=64)
    create_time=models.DateTimeField(auto_now=True)


class Article(models.Model):
    title=models.CharField(max_length=255)
    up_count=models.IntegerField()
    down_count=models.IntegerField()
    read_count=models.IntegerField()
    edit_count=models.IntegerField()
    create_time=models.DateTimeField(auto_now=True)
    user=models.ForeignKey('Userinfo')


class Content(models.Model):
    article=models.ForeignKey('Article')
    text=models.TextField()

class Comment(models.Model):
    article=models.ForeignKey('Article')
    user=models.ForeignKey('Userinfo')
    ccont=models.CharField(max_length=255)#ccont是评论内容
    create_time=models.DateTimeField(auto_now=True)

class UpDown(models.Model):
    user=models.ForeignKey('Userinfo')
    article=models.ForeignKey('Article')
    method_choice=(
        (0,'踩'),
        (1,'赞')
    )
    method=models.IntegerField(choices=method_choice)

    class Meta:
        unique_together=[
            ('user','article'),
        ]