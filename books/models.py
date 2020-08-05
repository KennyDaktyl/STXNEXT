from django.db import models

# Create your models here.


# class Author(models.Model):
#     author = models.CharField(verbose_name="Author", max_length=512)

#     class Meta:
#         ordering = ("author", )
#         verbose_name_plural = "Autorzy"

#     def __str__(self):
#         return self.author


# class Category(models.Model):
#     category = models.CharField(verbose_name="Category", max_length=512)

#     class Meta:
#         ordering = ("category", )
#         verbose_name_plural = "Kategorie"

#     def __str__(self):
#         return self.category


class Book(models.Model):
    book_Id = models.CharField(
        verbose_name="Book_ID", max_length=126)
    etag = models.CharField(
        verbose_name="etag", max_length=126)
    selfLink = models.TextField(
        verbose_name="selflink")

    class Meta:
        ordering = ("book_Id", )
        verbose_name_plural = "Books"

    def __str__(self):
        return str(self.book_Id)


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
        return str(self.name)+" : "+str(self.type_field)


class AttributeType(models.Model):
    type_name = models.CharField(max_length=32)

    class Meta:
        ordering = ("type_name",)
        verbose_name_plural = "Type fields"

    def __str__(self):
        return str(self.type_name)


class AttributeValue(models.Model):
    book_id = models.ForeignKey(
        "Book", on_delete=models.CASCADE, db_index=True)
    attribute_id = models.ForeignKey("Attribute", on_delete=models.CASCADE)
    attribute_value_str = models.TextField(null=True, blank=True)
    attribute_value_float = models.FloatField(null=True, blank=True)
    attribute_value_bool = models.BooleanField(null=True, blank=True)

    class Meta:
        ordering = ("book_id", "attribute_id")
        verbose_name_plural = "Attributes value"

    def __str__(self):
        return str(self.book_id)+"-"+str(self.attribute_id)
