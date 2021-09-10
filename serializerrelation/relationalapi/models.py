from django.db import models


class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='songs')
    duration = models.IntegerField()

    def __str__(self):
        return self.title
