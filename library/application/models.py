from django.db import models


class Publishing(models.Model):
    name = models.CharField(max_length=150)
    review = models.TextField()

    def __str__(self):
        return f"{self.pk} - {self.name}. Write please your opinion: {self.review}."


class Author(models.Model):
    publishing = models.ForeignKey(Publishing, on_delete=models.CASCADE,
                                   null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    birth_year = models.DateTimeField()

    def __str__(self):
        return f"{self.pk} - {self.first_name} {self.alias}, {self.last_name} {self.birth_year}. \
        You can find him in {self.publishing}"


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.pk} - {self.title} {self.price}. Author id = {self.author}"


