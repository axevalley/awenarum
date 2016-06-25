from django.db import models


class HomepageArticle(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=100)
    text = models.TextField()
    image = models.FileField()

    def __str__(self):
        return self.title + ' - ' + self.subtitle
