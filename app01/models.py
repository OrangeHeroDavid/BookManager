from django.db import models


# Create your models here.
class Publisher(models.Model):  # app01_publisher
    pid = models.AutoField(primary_key=True)  # pid 主键
    name = models.CharField(max_length=32, unique=True)  # 出版社名称

    # def __str__(self):
    #     return self.name


class Book(models.Model):
    title = models.CharField(max_length=32, unique=True)  # 书籍的名称
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)  # 关联了出版社
