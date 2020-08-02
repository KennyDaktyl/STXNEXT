from django.db import models

# Create your models here.


class Author(models.Model):
    author = models.CharField(verbose_name="Author", max_length=512)

    class Meta:
        ordering = ("author", )
        verbose_name_plural = "Autorzy"

    def __str__(self):
        return self.author


class Category(models.Model):
    category = models.CharField(verbose_name="Category", max_length=512)

    class Meta:
        ordering = ("category", )
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return self.category


class Book(models.Model):
    title = models.CharField(verbose_name="Title", max_length=512)
    authors = models.ManyToManyField('Author')
    published_date_year = models.IntegerField(verbose_name="Year",
                                              null=True,
                                              blank=True)
    categories = models.ManyToManyField('Category', blank=True)
    average_rating = models.FloatField(max_length=2, null=True, blank=True)
    ratings_count = models.IntegerField(null=True, blank=True)
    thumbnail = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ("title", )
        verbose_name_plural = "Książki"

    def __str__(self):
        return str(self.title) + "," + str(self.published_date_year)
