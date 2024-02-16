from django.db import models
from categories.models import Categories
from author.models import Author


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Categories)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE
    )  # Many to one er jonne use korbo foregin key; author profile delete kore dile tar ar kichu show korbe na

    def __str__(self):
        return self.title
