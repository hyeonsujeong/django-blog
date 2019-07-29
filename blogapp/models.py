from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.category

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title