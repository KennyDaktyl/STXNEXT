from django.db import models

# Create your models here.


class Author(models.Model):
    author = models.CharField(verbose_name="Author", max_length=512)

    class Meta:
        ordering = ("author", )

    def __str__(self):
        return self.author


class Category(models.Model):
    category = models.CharField(verbose_name="Category", max_length=512)

    class Meta:
        ordering = ("category", )

    def __str__(self):
        return self.category


class Book(models.Model):
    bookId = models.CharField(
        verbose_name="book_ID", max_length=126)
    etag = models.CharField(
        verbose_name="etag", max_length=126)
    selfLink = models.TextField(
        verbose_name="selflink")
    title = models.TextField(
        verbose_name="Title", null=True, blank=True)
    publishedDate = models.CharField(max_length=10,
                                     verbose_name="publishedDate", null=True, blank=True)
    authors = models.ManyToManyField("Author", blank=True)
    categories = models.ManyToManyField("Category", blank=True)
    averageRating = models.FloatField(null=True, blank=True)
    ratingsCount = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ("bookId", )
        verbose_name_plural = "Books"

    def __str__(self):
        return str(self.id)+":"+str(self.bookId)


class Attribute(models.Model):
    name = models.CharField(
        max_length=128, db_index=True, null=True, blank=True)
    parent_info = models.ForeignKey(
        "Attribute", on_delete=models.CASCADE, null=True, blank=True)
    type_field = models.ForeignKey(
        "AttributeType", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ("name", )
        verbose_name_plural = "Attributes"

    def __str__(self):
        return str(self.name)


class AttributeType(models.Model):
    type_name = models.CharField(max_length=32)

    class Meta:
        ordering = ("type_name",)
        verbose_name_plural = "Type fields"

    def __str__(self):
        return str(self.type_name)


class AttributeValue(models.Model):
    bookId = models.ForeignKey(
        "Book", on_delete=models.CASCADE, db_index=True)
    attributeId = models.ForeignKey(
        "Attribute", on_delete=models.CASCADE, null=True, blank=True)
    attribute_value_str = models.TextField(null=True, blank=True)
    attribute_value_float = models.FloatField(null=True, blank=True)
    attribute_value_bool = models.BooleanField(null=True, blank=True)
    attribute_value_list = models.TextField(null=True, blank=True)
    attribute_value_dict = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("bookId", "attributeId")
        verbose_name_plural = "Attributes value"

    def save(self, *args, **kwargs):
        book = Book.objects.get(pk=self.bookId.id)
        if str(self.attributeId.name) == 'title':
            book.title = self.attribute_value_str
            book.save()
        if str(self.attributeId.name) == 'publishedDate':
            book.publishedDate = self.attribute_value_str
            book.save()
        if str(self.attributeId.name) == 'authors' and type(self.attribute_value_list) != list and self.attribute_value_list != None:
            try:
                author = Author.objects.get(author=self.attribute_value_list)
            except:
                author = Author()
            author.author = self.attribute_value_list
            author.save()
            book.authors.add(author)
            book.save()
        if str(self.attributeId.name) == 'categories' and type(self.attribute_value_list) != list and self.attribute_value_list != None:
            try:
                category = Category.objects.get(
                    category=self.attribute_value_list)
            except:
                category = Category()
            category.category = self.attribute_value_list
            category.save()
            book.categories.add(category)
            book.save()
        if str(self.attributeId.name) == 'averageRating':
            book.averageRating = self.attribute_value_float
            book.save()
        if str(self.attributeId.name) == 'ratingsCount':
            book.ratingsCount = self.attribute_value_float
            book.save()
        super(AttributeValue, self).save()

    def __str__(self):
        return str(self.bookId)+"-"+str(self.attributeId)
