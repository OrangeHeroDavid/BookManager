from django.db import models


# Create your models here.
class Publisher(models.Model):  # app01_publisher
    pid = models.AutoField(primary_key=True)  # pid 主键
    name = models.CharField(max_length=32, unique=True)  # 出版社名称

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=32, unique=True)  # 书籍的名称
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)  # 关联了出版社

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=32, unique=True)  # 作者的名字
    books = models.ManyToManyField('Book')  # 表示作者和书籍 多对多的关系
    # books = models.ManyToManyField('Book', through='Author_book')  # 表示作者和书籍 多对多的关系

    def __str__(self):
        return self.name


# class Author_book(models.Model):
#     author = models.ForeignKey('Author')
#     book = models.ForeignKey('Book')
#     date = models.DateTimeField()
